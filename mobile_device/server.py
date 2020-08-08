#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 下午3:54
# @Author  : Boyka
# @Email   : upcvagen@163.com
# @Software: PyCharm

import base64
import threading

import cv2
import numpy as np
from flask import request, Flask

app = Flask(__name__)


def show_result(img):
    img = cv2.imread(img)
    cv2.imshow("image_window", img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


@app.route("/", methods=['POST', 'GET'])
def get_frame():
    # 解析图片数据
    res = request
    img = base64.b64decode(str(res.form['image']))
    image_data = np.fromstring(img, np.uint8)
    image_data = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    save_path = "1.jpg"
    cv2.imwrite(save_path, image_data)
    t = threading.Thread(target=show_result(save_path))
    t.start()
    return 200


if __name__ == "__main__":
    app.run("127.0.0.1", port=5005)
