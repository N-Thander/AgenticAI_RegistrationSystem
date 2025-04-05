
from fastapi import FastAPI, HTTPException 
from schemas import RegistrationRequest, RegistrationResponse
from crud import RegistrationBot

app = FastAPI()