
import subprocess

def extract_info_from_transcript(transcript):
    prompt = f"""You are an AI assistant. The speakers are not labeled, but it's a 1:1 conversation between a sales representative and a prospect. 
Extract the following from the sales call transcript:
- Contact name (if stated)
- Company name (if stated)
- Main pain points
- Objections (if any)
- Interest level
- Next steps

If any field is missing or unclear, set it to "Unknown" and confidence to "Low".
Return JSON with each field and a confidence score (High/Medium/Low).

Transcript:
\"\"\"{transcript}\"\"\"
"""
    result = subprocess.run(
    ['ollama', 'run', 'llama3', prompt],
    capture_output=True,
    text=True,
    encoding='utf-8'  
)

    return result.stdout
def generate_followup_email(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'llama3', prompt],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    return result.stdout.strip()
