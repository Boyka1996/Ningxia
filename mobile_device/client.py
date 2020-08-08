#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 下午3:54
# @Author  : Boyka
# @Email   : upcvagen@163.com
# @Software: PyCharm

import base64
import time

import requests

file_path = "/home/chase/datasets/dogs-vs-cats/test1/1.jpg"
start_time = time.time()
with open('/home/chase/datasets/dogs-vs-cats/test1/1.jpg', 'rb') as f:
    img = base64.b64encode(f.read()).decode()
image = []
image.append(img)
res = {"image": image, "info": "test info"}
# 访问服务
res = requests.post("http://127.0.0.1:5005", data=res)
print(res)
print(time.time() - start_time)
