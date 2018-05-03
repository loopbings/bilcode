# coding: utf-8

from PIL import Image  # 导入图片
import numpy as np  # 图片保存为矩阵,利用其进行矩阵运算

class Captcha:
    __rgb_img = None  # RGB格式的图片
    __rgb_mat = None  # RGB分量值为元素的矩阵
    __p_img = None  # 调色板格式的图片
    __p_mat = None  # 像素点为代表颜色的整数的矩阵

        
    # def __init__(self,img_uri):
    #     self.__rgb_img = Image.open(img_uri)
    def __init__(self,img):
        self.__rgb_img = img

    def rgb_img2mat(self):
        col=0
        cnt=0
        rgb_r=0
        rgb_g=0
        rgb_b=0

        for x in range(self.__rgb_img.size[0]):
            col = col + 1
            for y in range(self.__rgb_img.size[1]):
                pix = self.__rgb_img.getpixel((x, y))
                cnt = cnt + 1
                
                rgb_r+=pix[0]
                rgb_g+=pix[1]
                rgb_b+=pix[2]
                
                #print(pix)
        rgb_r//=cnt
        rgb_g//=cnt
        rgb_b//=cnt
        
        # print(str(cnt//col)+"行")
        # print(str(col)+"列")
        # print("RGB平均值")
        # print("R:"+str(rgb_r))
        # print("G:"+str(rgb_g))
        # print("B:"+str(rgb_b))


        
        background_r=0
        background_g=0
        background_b=0
        background_cnt=0
    
        font_r=0
        font_g=0
        font_b=0
        font_cnt=1

        limit = 1
        for x in range(self.__rgb_img.size[0]):
            for y in range(self.__rgb_img.size[1]):
                pix = self.__rgb_img.getpixel((x, y))
                if(pix[0]>rgb_r*limit or pix[1]>rgb_g*limit or pix[2]>rgb_b*limit):
                    background_cnt = background_cnt + 1
                    background_r = background_r + pix[0]
                    background_g = background_g + pix[1]
                    background_b = background_b + pix[2]
                else:
                    font_cnt = font_cnt +1
                    font_r = font_r + pix[0]
                    font_g = font_g + pix[1]
                    font_b = font_b + pix[2]
  
        
        background_r//=background_cnt
        background_g//=background_cnt
        background_b//=background_cnt

        # print("RGB背景色均值")
        # print("R:"+str(background_r))
        # print("G:"+str(background_g))
        # print("B:"+str(background_b))
        font_r//=font_cnt
        font_g//=font_cnt
        font_b//=font_cnt
        # print("RGB字体颜色均值")
        # print("R:"+str(font_r))
        # print("G:"+str(font_g))
        # print("B:"+str(font_b))
 
        limit = 0.5
        limit_r = background_r - (background_r - font_r)*limit
        limit_g = background_g - (background_g - font_g)*limit 
        limit_b = background_b - (background_b - font_b)*limit 

        for x in range(self.__rgb_img.size[0]):
            for y in range(self.__rgb_img.size[1]):
                pix = self.__rgb_img.getpixel((x, y))
                if(pix[0]> limit_r or pix[1]>limit_g or pix[2]>limit_b):
                    self.__rgb_img.putpixel((x,y),(255,255,255))
         
      


    def get_img(self):
        return self.__rgb_img