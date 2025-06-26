
import json
import os
from hubspot import HubSpot
from hubspot.crm.contacts import PublicObjectSearchRequest, Filter, FilterGroup
from hubspot.crm.objects.notes import SimplePublicObjectInputForCreate
from dotenv import load_dotenv
load_dotenv()
HUBSPOT_TOKEN = os.getenv("HUBSPOT_TOKEN")

hubspot = HubSpot(access_token="Bearer {HUBSPOT_TOKEN}") 

def search_contact_by_name(name):
    filter = Filter(property_name="firstname", operator="EQ", value=name)
    filter_group = FilterGroup(filters=[filter])
    search_request = PublicObjectSearchRequest(
        filter_groups=[filter_group],
        properties=["firstname", "lastname", "email"]
    )
    response = hubspot.crm.contacts.search_api.do_search(public_object_search_request=search_request)
    results = response.results
    return results[0].id if results else None

def create_note_for_contact(contact_id, summary_data: dict):
    content = f"Call Summary:\n\n{json.dumps(summary_data, indent=2)}"
    note_obj = SimplePublicObjectInputForCreate(properties={"hs_note_body": content})
    note = hubspot.crm.objects.notes.basic_api.create(simple_public_object_input_for_create=note_obj)
    hubspot.crm.objects.notes.associations_api.create(
        note.id, "contacts", contact_id, "note_to_contact"
    )
    return note.id
