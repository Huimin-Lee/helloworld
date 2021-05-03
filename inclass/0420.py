#取得圖片修改後回傳
import cv2
import numpy as np
import base64
from flask import make_response
from flask import render_template
from flask import url_for
import json
from flask import Flask, request, jsonify
app = Flask(__name__)



@app.route('/')
def index():
    # 顯示表單
    return render_template('form.html')

@app.route('/', methods=['POST'])
def process():
    # 取得上傳的圖片
    file1 = request.files['image1']
    # 讀取檔案內容
    file1_content = file1.read()
    # 將檔案內容轉為 Numpy Array
    npimg1 = np.fromstring(file1_content, np.uint8)
    # 將 Numpy Array 進行圖像解碼
    bgr1 = cv2.imdecode(npimg1, cv2.IMREAD_COLOR)

    # return jsonify(bgr1.shape)


    # 處理…前面省略…
    rgb1 = cv2.cvtColor(bgr1, cv2.COLOR_BGR2RGB)
    height, width = rgb1.shape[:2]
    radius = int(min(height, width) * 0.48)
    thickness = int(min(height, width) * 0.02)
    cv2.circle(rgb1, (int(width / 2), int(height / 2)), radius, (255, 0, 0), thickness)
    bgr1 = cv2.cvtColor(rgb1, cv2.COLOR_BGR2RGB)

     # …後面也省略…



    line_color_hex = request.form.get('line_color').lstrip('#')
    line_color_rgb = tuple(int(line_color_hex[i:i+2], 16) for i in (0, 2, 4))
    line_thickness = int(request.form.get('line_thickness'))
    # …中間也省略…

    thickness = int(min(height, width) * 0.01 *line_thickness)
    cv2.circle(rgb1, (int(width / 2), int(height / 2)),radius, line_color_rgb, thickness)
    # …後面繼續省略…

    return render_template('show_image.html', base64_image=base64_image)
