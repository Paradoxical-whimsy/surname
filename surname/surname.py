# -*- coding: utf-8 -*-                                                                                                                                                                                     关注公众号“和你学python”有更多惊喜哦~
#从PIL导入Image，ImageFont，ImageDraw模块
from PIL import Image, ImageFont, ImageDraw

#打开图片文件并赋值给img
img = Image.open('wallpaper.png')

#定义字体大小
font_size = 120

#打开已下载好的字体并赋值给font
font = ImageFont.truetype('aa十里八乡最可爱v1.1.ttf', font_size)

#新建一张宽为4倍字体大小，高为2倍字体大小用来放文字的透明图片
txt_img = Image.new('RGBA', (font_size * 4, font_size * 2))

#在txt_img上创建一个画笔对象draw
draw = ImageDraw.Draw(txt_img)

#调用draw的text()方法写入文字。
draw.text((0, 0), '惨绿青年\n发密且软', (253, 238, 205), font=font)

#调用rotatae方法旋转图片并赋值给txt
#第1个参数是旋转的角度，第2个参数表示旋转后的图片内容可以超出原来的范围
txt = txt_img.rotate(15, expand=True)

#调用paste()方法
img.paste(txt, (50, int(img.height / 3.2)), txt)

#保存为文件
img.save('surname.png')
