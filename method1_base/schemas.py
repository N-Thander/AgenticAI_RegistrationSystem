
from pydantic import BaseModel, EmailStr

class RegistrationRequest(BaseModel):
    message: str
    
class UserDetails(BaseModel):
    name: str
    email: EmailStr
    event: str
    
class RegistrationResponse(BaseModel):
    status: str
    registration_id: str