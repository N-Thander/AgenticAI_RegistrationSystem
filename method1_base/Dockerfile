
FROM python:3.10-slim

WORKDIR /app.py

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app.py/

# enter port no like 8000 for hugging face spaces
EXPOSE 1234

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "1234"]