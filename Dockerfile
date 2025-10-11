FROM docker.io/python:3.14.0
WORKDIR /code
COPY ./requirements.txt /code/requirement.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app

CMD ["fastapi", "run", "/code/app/main.py", "--port", "80"]
