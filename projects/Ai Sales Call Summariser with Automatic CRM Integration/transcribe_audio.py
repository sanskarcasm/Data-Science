import whisper
import os

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes an audio file into text using OpenAI's Whisper model.
    Returns the transcript as a string.
    """
    model = whisper.load_model("base")  # or "medium" / "large" for better accuracy
    result = model.transcribe(file_path)
    return result["text"]

def tag_speakers(transcript: str) -> str:
    lines = [line.strip() for line in transcript.strip().split("\n") if line.strip()]
    tagged = []
    speaker = "Sales Rep"
    for i, line in enumerate(lines):
        tagged.append(f"{speaker}: {line}")
        speaker = "Prospect" if speaker == "Sales Rep" else "Sales Rep"
    return "\n".join(tagged)
