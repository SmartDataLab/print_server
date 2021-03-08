import requests

with open("fastfile.py", "rb") as f:
    r = requests.post("http://10.46.123.59:8000/files", data={"file": f})
print(r.text)