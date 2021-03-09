import requests

with open("/Users/su/Documents/2020年度本科生党支部党支书述职报告.pdf", "rb") as f:  # README.md
    files = {"file": ("2020年度本科生党支部党支书述职报告.pdf", f, "multipart/form-data")}
    r = requests.post(
        url="http://10.46.123.59:8000/uploadfile/", files=files, allow_redirects=True
    )
print(r.text)