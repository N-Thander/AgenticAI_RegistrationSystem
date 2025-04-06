# Method 2 - Production

This is a actual production ready architecture for this project that can be modfied and scaled as per requirements or use case.


## Project Structure

```
college-fest-ai/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
├── config/
│   ├── __init__.py
│   └── settings.py
├── src/
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── groq_client.py
│   │   └── registration_flow.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── supabase_service.py
│   │   └── validation.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── tests/
│       ├── __init__.py
│       ├── test_registration.py
└── README.md

```