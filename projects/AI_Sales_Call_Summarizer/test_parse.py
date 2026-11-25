# test_parse.py
from extract import parse_llm_output

llm_output = """
Here is the extracted data in JSON format:

{
  "Contact Name": "Unknown",
  "Company Name": "Unknown",
  "Main Pain Points": [
    "Manual process of pulling reports takes a lot of time",
    "Marketing and sales data are in separate places, slowing down reporting"
  ],
  "Objections": [
    "Concern about the time it might take to get set up"
  ],
  "Interest Level": "High",
  "Next Steps": [
    "Send technical overview and pricing details",
    "Follow-up call next week"
  ]
}

Confidence scores:

Contact Name: Low
Company Name: Low
Main Pain Points: High
Objections: Medium
Interest Level: High
Next Steps: High
"""

parsed_data = parse_llm_output(llm_output)

print("\n--- Final Parsed Data ---")
for key, value in parsed_data.items():
    print(f"{key}: {value}")
