# gcp-pub-service
This app publish payloads to an xicorr service.

## Stack
- API: FastAPI
- API modularization: PyNest
- Serverless: GCP Cloud Run

## Get started

1. Create venv.
    ```bash
    python3.12 -m venv .venv
    ```

2. Source venv

    Using Windows:
    ```bash
    .venv/Scripts/activate
    ```

    Using macOS and Linux:
    ```bash
    source .venv/bin/activate
    ```

3. Install the dependencies.
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

## Usage

1. Run the server locally.

    ```bash
    $ python -m app
    ```
    To run the server: Go to the fastapi docs and use your api endpoints - lhost:8080/docs