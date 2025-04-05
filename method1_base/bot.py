import requests
from schemas import RegistrationRequest, UserDetails
from config import GROQ_API_ENDPOINT, GROQ_API_KEY

class RegistrationBot:
    def collect_user_details(self, request: RegistrationRequest) -> UserDetails:
        prompt = (
            "Extract the following information from the message: name, email, and event."
            "Message: " + request.message
        )
        
        headers = {
            
            "Authorization": "Bearer " + GROQ_API_KEY,
            "Content-Type": "application/json"
            
        }
        
        payload = {
            "query": prompt
        }
        
        response = requests.post(GROQ_API_ENDPOINT, json=payload, headers=headers)
        
        if response.status_code != 200:
            raise Exception("GROQ API request failed")
        
        result = response.json()
        
        try:
            name = result["name"]
            email = result["email"]
            event = result["event"]
        
        except KeyError:
            raise Exception("Failed to extract user details from message")
        
        return UserDetails(name=name, email=email, event=event)
        
        