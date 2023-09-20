from PIL import Image, ImageDraw, ImageFont
from math import *
import fractions
import excel_pars
fr_x = fractions.Fraction(1, 2000)
fr_y = fractions.Fraction(1, 200)
scale_y = 1 / 200
scale_x = 1 / 2000  # 5cm = 100m
scale_a5 = 8
def a5_paper(m=8):
    sheet = Image.new(mode='RGB', size=(420 * m, 297 * m), color=(255, 255, 255))
    return sheet
im = a5_paper()
dr = ImageDraw.Draw(im)
data = excel_pars.read_info()
text_size = int(15 * scale_a5 / 4)
font = ImageFont.truetype("arial.ttf", text_size)
head = f'   Продольный профиль\nмасштабы: вериткальный - {fr_y}\n                   горизонтальный - {fr_x}'
wd = len('Продольный профиль') / 2 * text_size
text = ['пикеты', 'расстояние', 'фактические отметки', 'уклоны', 'проектные отметки', 'расстояние', 'условный горизонт']
bottom = im.height - 5 * scale_a5
corner = 5 * scale_a5
dr.text((im.width / 2 - wd, 2 * scale_a5), head, font=font, fill=1)
for i in range(7):
    dr.line((corner, bottom - 12 * i * scale_a5, im.width - corner, bottom - 12 * i * scale_a5), fill=1)
    dr.text((corner, bottom - 12 * (i + 1) * scale_a5 + scale_a5 * 4), text[i], fill=1, font=font)
    usl_horizon = bottom - 12 * i * scale_a5
dr.line((45 * scale_a5, 20 * scale_a5, 45 * scale_a5, im.height - 5 * scale_a5), fill=1)

# pickets
pickets = excel_pars.find_pickets()
offset = 45 * scale_a5
x_of_point = []
for name, h_len in pickets.items():
    dr.line((offset, im.height - 17 * scale_a5, offset, im.height - 5 * scale_a5), fill=1)
    dr.text((offset - scale_a5, bottom), name, font=font, fill=1)
    offset += scale_a5 * 1000 * (100 - h_len[1]) * scale_x
    x_of_point.append(offset)
#im.show()
im.save('test.png')