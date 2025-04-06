# Method 1 - Basic Method 


This is just a base architecture for this project and was used for the initial prototype. 

## Project Structure

```
registration_bot/
├── app.py                # FastAPI application, registration endpoint
├── config.py             # Configuration settings (Supabase & GROQ API)
├── supabase_client.py    # Supabase client initialization
├── schemas.py            # Pydantic models for data validation
├── crud.py               # Functions for interacting with Supabase (inserting registration)
├── bot.py                # AI agent logic that calls the GROQ API to extract details
├── workflows.md          # Documentation of the registration workflow
├── requirements.txt      # List of Python dependencies
└── Dockerfile            # Containerization configuration (optional)

```