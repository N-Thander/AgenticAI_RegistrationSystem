

import logging
from typing import Dict, Optional
from groq import Groq
from config.settings import settings
from services.supabase_service import SupabaseManager
from models.schemas import RegistrationCreate, ErrorResponse
from utils.helpers import format_phone, validate_events_list, mask_email
import json

logger = logging.getLogger(__name__)

class RegistrationHandler:
    def __init__(self):
        self.groq_client = Groq(api_key=settings.GROQ_API_KEY)
        self.supabase = SupabaseManager()
        self.system_prompt = """You are a college fest registration assistant. Extract:
        - Full name
        - Valid email address
        - 10-digit phone number (Indian format)
        - College name
        - List of events from: {allowed_events}
        
        Return JSON with keys: name, email, phone, college, events"""

    async def process_registration(self, user_input: str) -> Dict:
        """Main registration workflow"""
        try:
            # Extract structured data using Groq
            parsed_data = self._parse_with_groq(user_input)
            
            # Validate and normalize data
            validated_data = self._validate_data(parsed_data)
            
            # Check for existing registration
            if self.supabase.check_existing_registration(validated_data["email"]):
                raise ValueError("Email already registered")
            
            # Save to database
            registration = self.supabase.create_registration(validated_data)
            
            return {
                "success": True,
                "registration_id": registration["id"],
                "events": validated_data["events"],
                "message": "Registration successful"
            }
            
        except Exception as e:
            logger.error(f"Registration failed: {str(e)}")
            return self._handle_error(e)

    def _parse_with_groq(self, user_input: str) -> Dict:
        """Use Groq API to parse natural language input"""
        try:
            response = self.groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt.format(
                            allowed_events=", ".join(settings.ALLOWED_EVENTS)
                        )
                    },
                    {"role": "user", "content": user_input}
                ],
                model="mixtral-8x7b-32768",
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            raise RuntimeError(f"AI parsing failed: {str(e)}")

    def _validate_data(self, raw_data: Dict) -> Dict:
        """Validate and clean registration data"""
        try:
            # Format phone number
            raw_data["phone"] = format_phone(raw_data["phone"])
            
            # Validate events
            raw_data["events"] = validate_events_list(
                raw_data["events"], 
                settings.ALLOWED_EVENTS
            )
            
            # Pydantic validation
            return RegistrationCreate(**raw_data).dict()
        except Exception as e:
            raise ValueError(f"Validation failed: {str(e)}")

    def _handle_error(self, error: Exception) -> Dict:
        """Format error response"""
        error_msg = str(error)
        if "validation" in error_msg.lower():
            error_type = "validation_error"
        elif "exists" in error_msg.lower():
            error_type = "duplicate_error"
        else:
            error_type = "server_error"
            
        return {
            "success": False,
            "error_type": error_type,
            "message": error_msg
        }