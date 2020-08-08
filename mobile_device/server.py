#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 下午3:54
# @Author  : Boyka
# @Email   : upcvagen@163.com
# @Software: PyCharm

import base64
import threading
import multiprocessing
import cv2
import numpy as np
from PIL import Image
from flask import request, Flask

app = Flask(__name__)


def show_result(img):

    # img = Image.open(img)
    # img.show(20)
    image_name=img
    img = cv2.imread(img)
    cv2.imshow("111", img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    print("Display Finished!")
    return


@app.route("/", methods=['POST', 'GET'])
def get_frame():
    # 解析图片数据
    res = request
    save_path = res.form['file_name']
    print(save_path)
    img = base64.b64decode(str(res.form['image']))
    image_data = np.fromstring(img, np.uint8)
    image_data = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    cv2.imwrite(save_path, image_data)
    p=multiprocessing.Process(target=show_result(save_path))
    p.start()
    # show_result(save_path)
    # t = threading.Thread(target=show_result(save_path))
    # t.setDaemon(True)
    # t.start()
    return "200"


if __name__ == "__main__":
    app.run("127.0.0.1", port=5005)
