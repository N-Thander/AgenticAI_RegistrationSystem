
import os
import json 
from groq import Groq
from config.settings import settings

class GroqRegistrationParser:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.system_prompt = """
        
        Extract regitration details from user input.
        
        - Name (full name)
        - Email (valid format)
        - Phone (10-digit Indian number)
        - College Name 
        - Events (comma separated from allowed list)
        
        Return  JSON format:
        {
            "name": "string",
            "email": "string",
            "phone": "string",
            "college": "string",
            "events": ["string"]
        }
        
        """
        
    def parse_registration(self, user_input):
        try:
            chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_input}
            ],
            model="",  # use some model
            temperature=0.1,
            response_format={"type": "json_object"}
        )
            return json.loads(chat_completion.choices[0].message.content)
        except Exception as e:
            raise ValueError(f"Groq parsing failed: {str(e)}")