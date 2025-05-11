FROM python:3.12-slim

WORKDIR /app

COPY code/ ./code

WORKDIR /app/code

RUN pip install --upgrade pip

CMD ["python3", "-m", "unittest", "test_calculadora.py"]
