import requests

with open("README.md", "rb") as f:
    r = requests.post("http://127.0.0.1:8000/files", files={"README.md": f})
print(r.text)