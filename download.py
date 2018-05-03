# coding: utf-8

import os
import requests
import time

def downloads_pic(pic_name):
    url = 'http://cccj.pku.edu.cn/getImgCode.do'
    res = requests.get(url, stream=True)

    print(res)

    with open('{}/picture/{}'.format(os.getcwd(),pic_name), 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:  # 过滤下保持活跃的新块
                f.write(chunk)

                f.flush()

        f.close()


if __name__ == '__main__':
    for i in range(10):
        pic_name = int(time.time() * 1000000)
        downloads_pic('{}.{}'.format(pic_name,'png'))
