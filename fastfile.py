from fastapi import FastAPI, File, UploadFile
import os
from sh import lp
import _thread
import time
import uvicorn
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
    printer_name = "HP-LaserJet-Professional-M1136-MFP"
    os.system("lp %s -d %s"%(filename, printer_name))
 
def write_file(threadName, filename,file):
    f= open(filename,"wb")
    f.write(file.file.read())


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    _thread.start_new_thread(write_file, ("Thread-0", "/home/pi/dev/print_server/data/demo.pdf", file, ) )
    _thread.start_new_thread(print_file, ("Thread-1", "/home/pi/dev/print_server/data/demo.pdf", ) )
    return {"success": "true"}

if __name__ == "__main__":
    uvicorn.run("fastfile:app", host="0.0.0.0", port=8000, log_level="info")
