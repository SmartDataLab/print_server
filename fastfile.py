from fastapi import FastAPI, File, UploadFile
import os
from sh import lp
import _thread
import time
app = FastAPI()

def print_file(threadName, filename):
    time.sleep(5)
    os.system("lp %s"%filename)
 
def write_file(threadName, filename,file):
    f= open(filename,"wb")
    f.write(file)

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    _thread.start_new_thread(write_file, ("Thread-0", "data/demo", file) )
    _thread.start_new_thread(print_file, ("Thread-1", "data/demo", ) )
    # lp("/home/pi/dev/print_server/data/demo")
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}