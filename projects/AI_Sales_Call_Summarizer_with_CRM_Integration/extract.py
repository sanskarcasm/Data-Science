import json
import re
def normalize_next_steps(raw):
    if isinstance(raw, dict):
        # Convert keys with True values into a list of strings
        return [k for k, v in raw.items() if v]
    elif isinstance(raw, list):
        return raw
    return ["Unknown"]

def get_any(data, *keys):
    """Try multiple key formats for flexibility."""
    for k in keys:
        if k in data:
            return data[k]
    return "Unknown"

def parse_next_steps(value):
    if isinstance(value, dict):
        return [step.replace("_", " ").capitalize() for step, v in value.items() if v]
    elif isinstance(value, list):
        return value
    elif isinstance(value, str):
        return [value]
    return ["Unknown"]


def parse_llm_output(llm_output):
    print("== LLM OUTPUT ==")
    print(llm_output)

    # Safely extract the JSON block from the LLM output
    json_match = re.search(r'\{[\s\S]+?\}', llm_output)
    if not json_match:
        print("⚠️ No JSON block found.")
        return {}

    try:
        raw_json = json_match.group(0)
        data = json.loads(raw_json)
        print("✅ Parsed JSON:", data)
    except json.JSONDecodeError as e:
        print("❌ JSON Decode Error:", e)
        print("Bad JSON:", raw_json)
        return {}
    

    # Map values using either snake_case or Title Case
    mapped = {
        "contact_name": get_any(data, "contact_name", "Contact Name"),
        "company": get_any(data, "company_name", "Company Name"),
        "pain_points": get_any(data, "main_pain_points", "Main Pain Points"),
        "objections": get_any(data, "objections", "Objections"),
        "interest_level": get_any(data, "interest_level", "Interest Level"),
        "next_steps": parse_next_steps(get_any(data, "next_steps", "Next Steps")),
        "confidence": {}
    }

    # Extract confidence scores (e.g., "Objections: Medium")
    conf_match = re.findall(r'\*? ?([A-Za-z ]+): (Low|Medium|High)', llm_output)
    for k, v in conf_match:
        key = {
     "contact name": "contact_name",
    "company name": "company",
    "main pain points": "pain_points",
    "objections": "objections",
    "interest level": "interest_level",
    "next steps": "next_steps"
}.get(k.strip().lower(), k.strip().lower().replace(" ", "_"))

        mapped["confidence"][key] = v

    print("✅ Final mapped object:", mapped)
    return mapped

def needs_review(confidence):
    """Return True if the confidence is not High."""
    return confidence.lower() != "high"
