from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()
REQUEST_COUNT = Counter("app_requests_total", "Total requests")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

@app.get("/todos")
def get_todos():
    REQUEST_COUNT.inc()
    return {"todos": []}
