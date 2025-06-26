
# AI Sales Call Summarizer

## Overview

The AI Sales Call Summarizer is an end-to-end tool designed to help sales teams automatically capture, structure, and act on insights from sales calls. By leveraging cutting-edge AI tools such as OpenAI's Whisper and Meta’s LLaMA 3, our solution transcribes audio, extracts key conversation insights, generates personalized follow-up emails, and updates HubSpot CRM—all with minimal manual intervention.

---

## Business Case & Problem Statement

Sales reps often spend up to 72% of their time on administrative tasks rather than selling. According to recent studies:
- Reps only spend **28%** of their week selling.
- **74%** of B2B deals are lost due to slow follow-up or poor call documentation.

This leads to:
- Inconsistent CRM data,
- Delayed or generic follow-up emails,
- Missed opportunities due to lost context from conversations.

Our tool addresses these issues by automating the entire post-call workflow so that every conversation is transformed into actionable insights.

---

## Technical Solution & Architecture

### Key Components

1. **Audio Transcription**  
   We use OpenAI Whisper to transcribe sales call audio into text. Whisper is chosen for its robust multi-language support and accuracy even with imperfect audio.

2. **Insight Extraction & Summarization**  
   We utilize Meta’s LLaMA 3 model to process transcripts. It extracts structured data (e.g., pain points, objections, interest level, next steps, contact information) and outputs a JSON summary. This approach allows us to:
   - Ensure consistent formatting for CRM uploads,
   - Allow reps to edit low-confidence fields via a Streamlit frontend.

3. **Follow-Up Email Generation**  
   The same LLaMA 3 model is used to generate personalized follow-up emails from the extracted data—ensuring clarity, context, and professionalism.

4. **CRM Integration (HubSpot)**  
   The system integrates with HubSpot using its API. It searches for an existing contact, creates one if not found, and attaches the summarized call details as a note.

### How It Works (Workflow)

1. **Input:** A rep either uploads a recorded sales call audio file or pastes the transcript into the application.
2. **Processing:**  
   - Audio files are transcribed.
   - The text is processed to extract key insights and structure them in JSON format.
   - A follow-up email draft is generated.
3. **Output:**  
   - The rep can review and edit the extracted fields.
   - The system saves the summary locally (as a JSON file) and provides a download option.
   - On command, the summary is pushed to HubSpot CRM (creating or updating the contact record) and a note is logged with the full details.

---

## Setup and Installation

### Prerequisites

- Python 3.9 or later
- Virtual environment (recommended)
- ffmpeg installed and added to your system PATH  
  (On Windows, download from [Gyan Dev](https://www.gyan.dev/ffmpeg/builds/) and add the `bin` folder to PATH)
- HubSpot Private App Token (see instructions below)

### Environment Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ai-sales-call-summarizer.git
   cd ai-sales-call-summarizer
Set Up a Virtual Environment:

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # on Windows, use: .venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Ensure that python-dotenv, streamlit, requests, hubspot-api-client (or relevant dependencies), and openai-whisper (or install directly from GitHub) are listed in your requirements.txt.

Create a .env File:

In the project root, create a file named .env and add:

env
Copy
Edit
HUBSPOT_TOKEN=your_private_app_token_here
Replace your_private_app_token_here with your actual HubSpot Private App token. (Note: Do not use an API key—HubSpot now requires private app tokens.)

Running the App
Launch the Streamlit app by running:

bash
Copy
Edit
streamlit run app.py
Using the App
Audio Input: Toggle the checkbox to use an audio file input. Upload your sales call recording (supports .wav, .mp3, or .m4a). The app transcribes the audio and shows the transcript.

Text Input: Alternatively, you can paste the transcript directly.

Extract Info: Click the "Extract Info" button. The app sends the transcript to our LLaMA 3-powered extraction system, which returns structured data (pain points, objections, etc.).

Review & Edit: Check the extracted fields and edit if necessary (for fields with low confidence).

Save: Save the data as a JSON file and optionally download it.

Generate Follow-Up Email: Generate a customized email draft based on the extracted data.

Update HubSpot CRM: Push the summary to HubSpot CRM. The app will search for the contact by name, create a new contact if not found, and attach the summary as a note.

Evaluation Criteria
We designed this project with the following evaluation dimensions in mind:

Your Thinking Process and Business Understanding:

We clearly identified the pain points in sales workflows and designed a solution that automates the tedious aspects of follow-up.

The project is grounded in real-world statistics and industry challenges.

Technical Execution and Development Practices:

The solution leverages modern, open-source AI tools (OpenAI Whisper and LLaMA 3) for efficient transcription and extraction.

It uses Streamlit for a user-friendly interface and integrates with HubSpot’s API for CRM updates.

The code is modular, well-documented, and designed with error handling and logging.

Leveraging AI Tools in Your Workflow:

AI is not used for the sake of it; it’s applied where it matters—automating repetitive tasks and extracting actionable insights.

Our use of LLaMA 3 ensures that the summaries and email drafts are both contextually accurate and personalized.

The overall workflow improves rep productivity and increases revenue potential.

Future Enhancements
Automated Speaker Diarization: Integrate more robust speaker labeling using advanced models (e.g., WhisperX or pyannote-audio).

Deeper CRM Integration: Extend beyond contacts and notes to automatically create tasks or deals in HubSpot.

Expanded Language Support: Enable multi-language transcription and summarization.

Real-Time Integration: Automate trigger events directly from call platforms (Zoom, Google Meet).

License
This project is open source and available under the MIT License.

Contact
For more information or collaboration, please contact Sanskar Pant at sanskaraugpant@gmail.com.
