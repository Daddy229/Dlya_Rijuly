from PIL import Image, ImageDraw, ImageFont
from math import *
import fractions
import excel_pars
import calc
def a5_paper(m=8):
    sheet = Image.new(mode='RGB', size=(420 * m, 297 * m), color=(255, 255, 255))
    return sheet
def usl_horizon(pics):
    heights = []
    for j in pics.values():
        heights.append(j[0])
    return int(min(heights) - 10)
pickets = excel_pars.find_pickets()
horizon = usl_horizon(pickets)
fr_x = fractions.Fraction(1, 2000)
fr_y = fractions.Fraction(1, 100)
scale_y = 1 / 100
scale_x = 1 / 2000  # 5cm = 100m
scale_a5 = 8
im = a5_paper()
dr = ImageDraw.Draw(im)
data = excel_pars.read_info()
text_size = int(15 * scale_a5 / 4)
font = ImageFont.truetype("arial.ttf", text_size)
bottom = im.height - 5 * scale_a5
head = f'   Продольный профиль\nмасштабы: вериткальный - {fr_y}\n                   горизонтальный - {fr_x}'
wd = len('Продольный профиль') / 2 * text_size
text = ['пикеты', 'расстояние', 'фактические отметки', 'уклоны', 'проектные отметки', 'расстояние',
        f'условный горизонт {usl_horizon(pickets)} m']
corner = 5 * scale_a5
dr.text((im.width / 2 - wd, 2 * scale_a5), head, font=font, fill=1)
usl_horizon_line = 0

for i in range(7):
    if i != 0:
        dr.line((corner, bottom - 12 * i * scale_a5, im.width - corner, bottom - 12 * i * scale_a5), fill=1)
    dr.text((corner, bottom - 12 * (i + 1) * scale_a5 + scale_a5 * 4), text[i], fill=1, font=font)
    usl_horizon_line = bottom - 12 * i * scale_a5
dr.line((55 * scale_a5, 20 * scale_a5, 55 * scale_a5, im.height - 65 * scale_a5), fill=1)
dr.text((52 * scale_a5, 15 * scale_a5), 'H, m', font=font, fill=1)
dr.line((55 * scale_a5, im.height - 53 * scale_a5, 55 * scale_a5, im.height - 41 * scale_a5), fill=1)

# delta pickets
delta = ['']
pic_len = list(pickets.values())
first = pic_len[0][1]
for i in pic_len[1:]:
    sec = i[1]
    if i[1] == 0:
        sec = 100
    delta.append(str(sec - first))
    first = i[1]

# pickets
offset_corner = 55 * scale_a5
x_of_point = []
step = scale_a5 * 1000 * 100 * scale_x
step_count = -1
offset = offset_corner
delta_c = 0
for name, h_len in pickets.items():
    if delta[delta_c] != '':    #kostil
        dr.text((offset + int(delta[delta_c]) * step // 200 - text_size * 0.3 * len(delta[delta_c]),
                 im.height - 25 * scale_a5), delta[delta_c], font=font, fill=1)
    delta_c += 1
    if h_len[1] != 0:
        offset = step * step_count + offset_corner + step / 100 * h_len[1]
    else:
        step_count += 1
        offset = step * step_count + offset_corner
    x_of_point.append(offset)
    dr.line((offset, im.height - 29 * scale_a5, offset, im.height - 17 * scale_a5), fill=1)
    dr.text((offset - scale_a5, bottom - 8 * scale_a5), name, font=font, fill=1)
    txt = Image.new(mode='RGB', size=(text_size * len(str(h_len[0])) // 2, text_size), color=(255, 255, 255))
    txt_dr = ImageDraw.Draw(txt)
    txt_dr.text((0, 0), str(h_len[0]), font=font, fill=1)
    txt = txt.rotate(90, expand=True)
    x, y = int(offset - scale_a5 * 2), int(im.height - 39.5 * scale_a5)
    lx, ly = txt.size
    im.paste(txt, (x, y, x + lx, y + ly))

spec = [i[0] for i in pickets.values()]
fx = x_of_point[0]
fy = usl_horizon_line - (spec[0] - horizon) * scale_y * 1000 * scale_a5
for ind, i in enumerate(spec[1:]):
    print(fx, fy,
          x_of_point[ind + 1], usl_horizon_line - (i - horizon) * scale_y * 1000 * scale_a5)
    dr.line((fx, fy, x_of_point[ind + 1], usl_horizon_line - (i - horizon) * scale_y * 1000 * scale_a5),
            fill=1, width=int(scale_a5/2))
    fx = x_of_point[ind + 1]
    fy = usl_horizon_line - (i - horizon) * scale_y * 1000 * scale_a5
    dr.line((fx, fy, fx, usl_horizon_line), fill=1)

trail = calc.volume_algo(pickets)[:2]
work = calc.volume_algo(pickets)[2:]
print(work)
offset_corner = 55 * scale_a5
fx = x_of_point[0]
const_x = fx
fy = usl_horizon_line - (spec[0] - horizon) * scale_y * 1000 * scale_a5
for i in trail:
    dr.line((fx, fy, i[1] * scale_a5 * scale_x * 1000 + const_x,
             usl_horizon_line - (i[0] - horizon) * scale_y * 1000 * scale_a5), fill='red', width=int(scale_a5/2))
    fy = usl_horizon_line - (i[0] - horizon) * scale_y * 1000 * scale_a5
    fx += i[1] * scale_a5 * scale_x * 1000
print(trail)
im.show()
im.save('test1.png')