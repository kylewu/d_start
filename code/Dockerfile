FROM python:3

COPY ./src /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

# Run the server when container is launched
CMD ["python", "main.py"]
