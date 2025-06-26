import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
HUBSPOT_TOKEN = os.getenv("HUBSPOT_TOKEN")

HUBSPOT_API_BASE = "https://api.hubapi.com"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {HUBSPOT_TOKEN}"  
}


def find_contact_by_name(name):
    """Search contact by first name"""
    url = f"{HUBSPOT_API_BASE}/crm/v3/objects/contacts/search"
    payload = {
        "filterGroups": [{
            "filters": [{
                "propertyName": "firstname",
                "operator": "EQ",
                "value": name
            }]
        }],
        "properties": ["firstname", "lastname", "email"]
    }
    res = requests.post(url, headers=HEADERS, json=payload)
    results = res.json().get("results", [])
    return results[0] if results else None


def create_contact(first_name, last_name="Unknown", email=None):
    """Create contact"""
    url = f"{HUBSPOT_API_BASE}/crm/v3/objects/contacts"
    props = {"firstname": first_name, "lastname": last_name}
    if email:
        props["email"] = email
    payload = {"properties": props}
    res = requests.post(url, headers=HEADERS, json=payload)
    res.raise_for_status()
    return res.json()


def create_note_for_contact(contact_id, note_body):
    """Create note and associate with contact"""
    url = f"{HUBSPOT_API_BASE}/crm/v3/objects/notes"
    payload = {
        "properties": {
            "hs_note_body": note_body
        },
        "associations": [
            {
                "to": {"id": contact_id},
                "types": [{"associationCategory": "HUBSPOT_DEFINED", "associationTypeId": 202}]
            }
        ]
    }
    res = requests.post(url, headers=HEADERS, json=payload)
    res.raise_for_status()
    return res.json()


def update_crm_with_summary(summary_dict):
    contact_name = summary_dict["contact_name"]
    note_body = json.dumps(summary_dict, indent=2)

    # 1. Try finding contact
    contact = find_contact_by_name(contact_name)

    # 2. If not found, create it
    if not contact:
        print(f"🔍 Contact '{contact_name}' not found. Creating new...")
        contact = create_contact(first_name=contact_name)
    else:
        print(f"✅ Found contact '{contact_name}'.")

    contact_id = contact["id"]

    # 3. Add note
    print(f"📝 Adding note to contact ID: {contact_id}")
    note = create_note_for_contact(contact_id, note_body)
    print("✅ Note added with ID:", note["id"])
