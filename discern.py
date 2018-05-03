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
    # rootdir = '{}/picture/'.format(os.getcwd())
    # list = os.listdir(rootdir)
    # filename='{}/{}'.format(os.getcwd(),'result.txt')
    # 遍历所有文件路径
    # piclist = []
    # for i in range(0, len(list)):
    #     path = os.path.join(rootdir, list[i])
    #     if os.path.isfile(path):
    #         piclist.append(path)
    # 验证码list
    # codelist = []
    # for str_path in piclist:
        path = '{}/picture/{}'.format(os.getcwd(),'1525348077163796.png')
        # path = str_path
        im = Image.open(path)
        im.show()
        # 水滴算法
        captchainfo = Captcha(im)
        captchainfo.rgb_img2mat()
        im = captchainfo.get_img()
        im.show()
        # 拆分
        im = binarizing(im, 150)
        # 降噪
        im = depoint(im)
        im.show()
        # 转换
        text = pytesseract.image_to_string(im, config='-psm 7')
        print(text)
    #     codelist.append('{}  {} \n'.format(path, text))
    # # 写入文件
    # with open(filename,'a') as f:
    #     for code in codelist:
    #         f.write(code)
