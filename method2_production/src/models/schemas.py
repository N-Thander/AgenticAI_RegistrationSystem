
from pydantic import BaseModel, validator, EmailStr, Field
from typing import List, Optional
from datetime import datetime 
from config.settings import settings
import re

class RegistrationBase(BaseModel):
    name: str = Field(..., min_length=3, example="Rahul Sharma")
    email: str = Field(..., example="rahul@college.edu.in")
    phone: str = Field(..., examples="9876543210")
    college: str = Field(..., min_length=4, example="ABC University")
    events: List[str] = Field(..., example=["workshop", "quiz"]) # list of event names
    
class RegistrationRequest(RegistrationBase):
    
    @validator("email")
    def validate_email(cls, v):
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", v):
            raise ValueError("Invalid email format")
        return v.lower()
    
    @validator("phone")
    def validate_phone(cls, v):
        cleaned = re.sub(r'\D', '', v)
        if len(cleaned) != 10:
            raise ValueError("Phone must be 10 digits")
        return cleaned
    
    @validator("events")
    def validate_events(cls, v):
        allowed = [events.lower() for events in settings.ALLOWED_EVENTS]
        invalid_events = [event for event in v if event.lower() not in allowed]
        
        if invalid_events:
            raise ValueError(f"Invalid events: {', '.join(invalid_events)}. Allowed events: {', '.join(allowed)}")
        return [event.lower() for event in v]
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Alice Smith",
                "email": "aOoT5@example.com",
                "phone": "1234567890",
                "college": "ABC University",
                "events": ["workshop", "quiz"]
            }
        }
        
        
class RegsistrationResponse(BaseModel):
    id: int
    created_at : datetime
    updated_at : Optional[datetime] = None
    
    class Config:
        orm_mode = True
        schmea_extra = {
            "example": {
                "id": 123,
                "created_at": "2023-05-01T12:34:56.789Z",
                "updated_at": "2023-05-02T12:34:56.789Z"
            }
        }