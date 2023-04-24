FROM python:3.10-alpine

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000"]