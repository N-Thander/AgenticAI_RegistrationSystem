
from supabase_client import supabase
from schemas import UserDetails
from datetime import datetime

def create_registration(details: UserDetails) -> dict:
    data = {
        "name": details.name,
        "email": details.email,
        "event": details.event,
        "registered_at": datetime.utcnow().isoformat(),
    }
    
    response = supabase.table("registrations").insert(data).execute()
    
    if response.get("error"):
        raise Exception(response["error"]["message"])
    
    
    inserted = response.get("data")[0]
    return inserted