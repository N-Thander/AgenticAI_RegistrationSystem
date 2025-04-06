
from fastapi import FastAPI, HTTPException 
from schemas import RegistrationRequest, RegistrationResponse
from crud import RegistrationBot

app = FastAPI()
bot = RegistrationBot()

@app.post("/registration", response_model=RegistrationResponse)
async def register(request: RegistrationRequest):
    try:
        user_details = bot.collect_user_details(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    try:
        registration = bot.create_registration(user_details)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"status": "success", "registration_id": registration["id"]}