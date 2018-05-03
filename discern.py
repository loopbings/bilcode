# coding: utf-8

import os
import pytesseract
from PIL import Image
from captcha import(
    Captcha
)

def binarizing(img, threshold):
    """传入image对象进行灰度、二值处理"""
    img = img.convert("L")  # 转灰度
    pixdata = img.load()
    w, h = img.size
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


def depoint(img):
    """传入二值化后的图片进行降噪"""
    pixdata = img.load()
    w, h = img.size
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 245:  # 上
                count = count + 1
            if pixdata[x, y + 1] > 245:  # 下
                count = count + 1
            if pixdata[x - 1, y] > 245:  # 左
                count = count + 1
            if pixdata[x + 1, y] > 245:  # 右
                count = count + 1
            if pixdata[x - 1, y - 1] > 245:  # 左上
                count = count + 1
            if pixdata[x - 1, y + 1] > 245:  # 左下
                count = count + 1
            if pixdata[x + 1, y - 1] > 245:  # 右上
                count = count + 1
            if pixdata[x + 1, y + 1] > 245:  # 右下
                count = count + 1
            if count > 5:
                pixdata[x, y] = 255
    return img

if __name__ == '__main__':
    path = '{}/picture/{}'.format(os.getcwd(),'1525344149253753.png')
    im = Image.open(path)
    im.show()
    # 水滴算法
    captchainfo = Captcha(im)
    captchainfo.rgb_img2mat()
    binaryImage = captchainfo.get_img()
    binaryImage.show()
    # 拆分
    binaryImage = binarizing(binaryImage, 150)
    # 降噪
    binaryImage = depoint(binaryImage)
    # 展示
    binaryImage.show()
    # 转换
    text = pytesseract.image_to_string(binaryImage, config='-psm 7')
    print(text)
