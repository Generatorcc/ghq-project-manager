"""GoHighLevel integration service functions."""

from src.modules.shared.utils import ghl_api_request

def get_ghl_contacts(token):
    """Fetch contacts from GoHighLevel."""
    return ghl_api_request("GET", "/contacts/", token)

def create_ghl_contact(token, contact_data):
    """Create a new contact in GoHighLevel."""
    return ghl_api_request("POST", "/contacts/", token, data=contact_data)
