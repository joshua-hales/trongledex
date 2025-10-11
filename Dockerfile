FROM docker.io/python:3.14.0
WORKDIR /code
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY app ./app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]
