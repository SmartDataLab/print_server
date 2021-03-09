# 小黑屋自主打印机

## 材料

- 打印机型号HP LaserJet Professional M1136 MFP
- [hp打印机linux驱动](https://www.freeprintersupport.com/download-hp-laserjet-pro-m1136-driver/)
- [fastapi接收文件相关文档](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/)

## dependency

- fastapi
- uvicorn

## 工程设计

- 搞懂win-api代码
- 多线程连接文件，换成restapi接收文件

## quick printer dependency 

```bash
sudo apt-get update
sudo apt-get install cups hplip
sudo usermod -a -G lpadmin pi # pi is your username
sudo hp-setup -i
lpstat -t
lp yourfile
```

## usage

- port 631 is cups interface
- uvicorn fastfile:app --reload --host 0.0.0.0
- http://ip:8000/docs is uvicorn interface for your debugging
- post a file use form like {"file": file : binary} to ip:8000

## TODO

<<<<<<< HEAD
- only post the final line 
- file binary io

307 Temporary Redirect

the final problem is i post to /uploadfile but the real url is /uploadfile/. it search and redirect me to the /uploadfile/. for small file, redirect will not lost, for large file, it will fail
=======
- only post the final line 
>>>>>>> 450ccbf96e67718fb5ccc0db96f7ad50f3bd06bc
