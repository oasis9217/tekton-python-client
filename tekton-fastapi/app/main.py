import sys
import signal
import urllib3
import uvicorn
from fastapi import Depends, FastAPI

from .dependencies import tekton_client
from .routers import pipelines, tasks

DEFAULT_NAMESPACE = "isw-tools"
urllib3.disable_warnings()

app = FastAPI()
app.include_router(pipelines.router)
app.include_router(tasks.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


@app.on_event("startup")
async def startup_event():
    signal.signal(signal.SIGINT, receive_signal)


def receive_signal(signal_number, frame):
    print('Received:', signal_number)
    sys.exit()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
