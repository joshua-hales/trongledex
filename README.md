# Trongledex

Provides a web API for access to descriptions of Trongle variations.

Designed for a tutorial on documentation practices.
The [presentation](./documentation-presentation.md) is designed for [maaslalani/slides](https://github.com/maaslalani/slides).


## Development

Install necessary dependencies and set up development tools with the following commands:

```
pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
```


## Run Locally

### Local

Run `pip install -r requirements.txt` to install necessary dependencies.

Run `uvicorn app.main:app --reload` to start the app.
Visit <http://127.0.0.1:8000/docs/> to see the interactive API documentation.

Stop with `CTRL+C`.


### Docker

Run `docker compose up` to start the app.
Visit <http://127.0.0.1:8000/docs/> (or your computer's hostname) to see the interactive API documentation.

Stop with `docker compose down`.
