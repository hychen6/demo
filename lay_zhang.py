from PIL import Image, ImageDraw, ImageFont
import cv2
import os


img = cv2.imread('boss.jpg')
img = img[:, :, (2, 1, 0)]

blank = Image.new("RGB", [len(img[0]), len(img)], "white")
drawObj = ImageDraw.Draw(blank)

n = 15

font = ImageFont.truetype('STHeiti Medium.ttc', size=n - 1)

for i in range(0, len(img), n):
    for j in range(0, len(img[i]), n):
        text = '张艺兴牛掰'
        drawObj.ink = img[i][j][0] + img[i][j][1] * 256 + img[i][j][2] * 256 * 256
        drawObj.text([j, i], text[int(j / n) % len(text)], font=font)
        print('完成处理——', i, j)

blank.save('lay_zhang.jpg' , 'jpeg')