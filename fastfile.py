from fastapi import FastAPI, File, UploadFile
import os
from sh import lp
import _thread
import time
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def print_file(threadName, filename):
    time.sleep(5)
    os.system("lp %s" % filename)


def write_file(threadName, filename, file):
    f = open(filename, "wb")
    f.write(file.file.read())


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    _thread.start_new_thread(
        write_file,
        (
            "Thread-0",
            "data/demo.pdf",
            file,
        ),
    )
    _thread.start_new_thread(
        print_file,
        (
            "Thread-1",
            "data/demo.pdf",
        ),
    )
    return {"success": "true"}