
from supabase import create_client
from config.settings import settings
import logging

class SupabaseManager:
    def __init__(self):
        self.client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        self.logger = logging.getLogger(__name__)
        
    def create_registration(self, data: dict):
        try:
            response = self.client.table('registrations').insert(data).execute()
            if not response.data:
                raise ValueError("No data received from Supabase")
            return response.data[0]            
        except Exception as e:
            self.logger.error(f"Supabase error: {str(e)}")
            raise RuntimeError("Registration storage failed")
        
        
    def check_existing_registration(self, email: str):
        try:
            repsonse = self.client.table('registrations').select("email").eq("email", email).execute()
            return len(repsonse.data) > 0
        except Exception as e:
            raise RuntimeError("Duplicate check failed")