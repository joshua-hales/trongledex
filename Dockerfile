FROM python:3
WORKDIR /code
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY app ./app
