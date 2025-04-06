
FROM python:3.10-slim

WORKDIR /app
COPY requiremtents.txt .

RUN pip install --no-cache-dir -r requiremtents.txt

COPY . . 

# replace with actual port no 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1234"]