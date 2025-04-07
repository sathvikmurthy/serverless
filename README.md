# Serverless Function Execution Platform

A lightweight serverless function executor using FastAPI, Docker, and Streamlit.

## Setup MongoDB

Ensure MongoDB is running locally or update the `MONGO_URI` environment variable.

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn backend.main:app --reload
```

## Run Frontend

```bash
streamlit run frontend/app.py
```
