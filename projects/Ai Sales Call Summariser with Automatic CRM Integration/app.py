import streamlit as st
from datetime import datetime
import json

from llm_utils import extract_info_from_transcript, generate_followup_email
from extract import parse_llm_output, needs_review
from transcribe_audio import transcribe_audio  # Optional: tag_speakers
from update_or_create_contact_and_note import update_crm_with_summary
from hubspot_utils import search_contact_by_name, create_note_for_contact

st.set_page_config(page_title="AI Sales Call Summarizer", layout="wide")
st.title("🧠 AI Sales Call Summarizer")

# Option to use audio or paste text
use_audio = st.checkbox("Use audio file instead of pasting transcript")

if use_audio:
    st.subheader("Upload Audio File")
    audio_file = st.file_uploader("Upload a .wav or .mp3 file", type=["wav", "mp3", "m4a"])
    if audio_file and "transcript" not in st.session_state:
        with open("temp_audio.mp3", "wb") as f:
            f.write(audio_file.read())

        with st.spinner("Transcribing audio..."):
            transcript = transcribe_audio("temp_audio.mp3")
            st.session_state["transcript"] = transcript
            st.success("Transcription complete!")
            st.text_area("Transcript:", transcript, height=300)
    transcript = st.session_state.get("transcript", "")
else:
    st.subheader("Paste Transcript")
    transcript = st.text_area("Paste your sales call transcript here:", height=300)

# Session state
if "extracted_data" not in st.session_state:
    st.session_state["extracted_data"] = None

# Extract info from transcript
if st.button("🧠 Extract Info"):
    if not transcript.strip():
        st.warning("Please provide a transcript first.")
    else:
        with st.spinner("Extracting..."):
            llm_output = extract_info_from_transcript(transcript)
            st.write("🤖 LLM Raw Output", llm_output)
            parsed = parse_llm_output(llm_output)
            st.session_state["extracted_data"] = parsed
            st.write("🔎 Parsed Extracted Data", parsed)

# Display/edit extracted data
data = st.session_state["extracted_data"]
if isinstance(data, dict) and data:
    st.subheader("📋 Review Extracted Fields")
    editable = {}

    for field in ["contact_name", "company", "pain_points", "objections", "interest_level", "next_steps"]:
        value = data.get(field, "Unknown")
        confidence = data.get("confidence", {}).get(field, "Low")
        label = f"{field.replace('_', ' ').title()} (Confidence: {confidence})"
        if needs_review(confidence):
            editable[field] = st.text_input(label, str(value))
        else:
            st.markdown(f"**{label}**")
            st.write(value)

    # Merge editable inputs
    saved_data = {**data, **editable}

    # Save to local JSON
    if st.button("💾 Save JSON"):
        st.success("Saved!")
        st.json(saved_data)
        filename = f"{saved_data.get('company', 'Unknown').replace(' ', '_')}_{datetime.now().strftime('%Y-%m-%d')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(saved_data, f, ensure_ascii=False, indent=2, default=str)
        with open(filename, "rb") as f:
            st.download_button("⬇️ Download JSON", data=f, file_name=filename, mime="application/json")

    # Generate email
    if st.button("✉️ Generate Follow-Up Email"):
        email_prompt = (
            f"Write a clear and professional follow-up email to a prospect named {saved_data.get('contact_name', 'Unknown')} "
            f"at {saved_data.get('company', 'Unknown')}. Thank them for their time on the sales call. "
            f"Summarize their exact pain points and objections from the list below. "
            f"Do not use placeholders like '[insert topic]' — be specific. "
            f"Conclude with the next steps.\n\n"
            f"Details:\n"
            f"- Pain Points: {saved_data.get('pain_points', 'Unknown')}\n"
            f"- Objections: {saved_data.get('objections', 'Unknown')}\n"
            f"- Interest Level: {saved_data.get('interest_level', 'Unknown')}\n"
            f"- Next Steps: {saved_data.get('next_steps', 'Unknown')}\n"
        )
        email_output = generate_followup_email(email_prompt)
        st.subheader("📧 Follow-Up Email Draft")
        st.markdown(email_output)

    # Update to HubSpot
    if st.button("📬 Update to HubSpot CRM"):
        contact_name = saved_data.get("contact_name", "").strip()
        if not contact_name:
            st.error("❌ No contact name found. Please extract or enter one.")
        else:
            with st.spinner("Checking for existing contact..."):
                contact_id = search_contact_by_name(contact_name)

            if contact_id:
                note_id = create_note_for_contact(contact_id, saved_data)
                st.success(f"✅ Note {note_id} created for contact '{contact_name}'")
            else:
                st.warning(f"⚠️ Contact '{contact_name}' not found. Creating one...")
                new_contact_id = update_crm_with_summary(saved_data)
                if new_contact_id:
                    st.success(f"✅ New contact '{contact_name}' created and note added.")
                else:
                    st.error("❌ Failed to create contact or note.")

# Debug/test button for dev only
if st.sidebar.checkbox("🔧 DEV: Test with fake summary"):
    if st.sidebar.button("Send Fake Summary to HubSpot"):
        summary_data = {
            "contact_name": "Swajit",
            "company": "Test Corp",
            "pain_points": ["Fake pain"],
            "objections": ["Fake objection"],
            "interest_level": "High",
            "next_steps": ["Follow up next week"],
            "confidence": {"contact_name": "High"}
        }
        update_crm_with_summary(summary_data)
        st.sidebar.success("Sent test summary to CRM.")
