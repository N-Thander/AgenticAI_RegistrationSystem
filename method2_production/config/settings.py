
import os
from dotenv import load_dotenv 

load_dotenv()

class Settings:
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    ALLOWED_EVENTS = os.getenv("ALLOWED_EVENTS").split(",")  
    
settings = Settings()