
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from core.groq_client import GroqRegistrationParser
from services.supabase_service import SupabaseManager
from services.validation import ResgistrationData
import logging

app = FastAPI()
parser = GroqRegistrationParser()
supabase = SupabaseManager()
logger = logging.getLogger("uvicorn.error")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
async def handle_registration(user_input: str):
    try:
        raw_data = parser.parse_registration(user_input)
        
        validated = ResgistrationData(**raw_data).dict()
        
        if supabase.check_existing_registration(validated["email"]):
            raise ValueError("Email already registered")
        
        result = supabase.create_registration(validated)
        
        return {
            "status": "success",
            "registration_id": result["id"],
            "events": validated["events"]
        }
        
    except Exception as e:
        logger.error(f"Registration error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))