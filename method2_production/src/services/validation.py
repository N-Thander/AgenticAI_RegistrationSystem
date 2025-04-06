
import re
from pydantic import BaseModel, validator, Field
from typing import List
from config.settings import settings


class RegistrationRequest(BaseModel):
    name: str = Field(..., min_length=3)
    email: str
    phone: str
    college: str
    events: List[str]
    
    @validator("email")
    def validate_email(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError("Invalid email format")
        return v.lower()
    
    @validator("phone")
    def validate_phone(cls, v):
        cleaned = re.sub(r"\D", "", v)
        if len(cleaned) != 10:
            raise ValueError("Invalid phone number")
        return cleaned
    
    @validator("events")
    def validate_events(cls, v):
        allowed = settings.ALLOWED_EVENTS
        invalid = [event for event in v if event.lower() not in allowed]
        if invalid:
            raise ValueError(f"Invalid events: {', '.join(invalid)}")
        return [event.lower() for event in v]