from PIL import Image, ImageDraw, ImageFont
import fractions
import excel_pars
import calc


def a5_paper(m=8):
    sheet = Image.new(mode='RGB', size=(420 * m, 297 * m), color=(255, 255, 255))
    return sheet

def usl_horizon(pics):
    heights = []
    pics_h = [h[0] for h in pics.values()]
    subtract = min(pics_h) // 4
    for j in pics.values():
        heights.append(j[0])
    return int(min(heights) - subtract)

def draw_profile(m_x_scale=2000, m_y_scale=200, profile_name='example'):
    pickets = excel_pars.find_pickets(f'{profile_name}.xlsx')
    fr_x = fractions.Fraction(1, m_x_scale)
    fr_y = fractions.Fraction(1, m_y_scale)
    scale_y = 1 / m_y_scale
    scale_x = 1 / m_x_scale
    scale_a5 = 8

    im = a5_paper()
    dr = ImageDraw.Draw(im)
    text_size = int(15 * scale_a5 / 4)
    font = ImageFont.truetype("arial.ttf", text_size)

    bottom = im.height - 5 * scale_a5
    corner = 5 * scale_a5
    head = f'   Продольный профиль\nмасштабы: вериткальный - {fr_y}\n                   горизонтальный - {fr_x}'
    wd = len('Продольный профиль') / 2 * text_size
    text = ['пикеты', 'расстояние', 'фактические отметки', 'уклоны', 'проектные отметки', 'расстояние',
            f'условный горизонт {usl_horizon(pickets)} m']
    dr.text((im.width / 2 - wd, 2 * scale_a5), head, font=font, fill=1)
    usl_horizon_line = 0

    # разлиновка листа
    for i in range(7):
        if i != 0:
            dr.line((corner, bottom - 12 * i * scale_a5, im.width - corner, bottom - 12 * i * scale_a5), fill=1)
        dr.text((corner, bottom - 12 * (i + 1) * scale_a5 + scale_a5 * 4), text[i], fill=1, font=font)
        usl_horizon_line = bottom - 12 * i * scale_a5

    dr.line((55 * scale_a5, 20 * scale_a5, 55 * scale_a5, im.height - 65 * scale_a5), fill=1)
    dr.text((52 * scale_a5, 15 * scale_a5), 'H, m', font=font, fill=1)
    dr.line((55 * scale_a5, im.height - 53 * scale_a5, 55 * scale_a5, im.height - 41 * scale_a5), fill=1)

    # поиск расстояния между пикетами
    delta = ['']
    pic_len = list(pickets.values())
    first = pic_len[0][1]
    for i in pic_len[1:]:
        sec = i[1]
        if i[1] == 0:
            sec = 100
        delta.append(str(sec - first))
        first = i[1]

    # заполнение таблицы пикетами
    offset_corner = 55 * scale_a5   # отступ начальный
    x_of_point = []
    step = scale_a5 * 1000 * 100 * scale_x
    step_count = -1
    offset = offset_corner
    delta_c = 0
    for name, h_len in pickets.items():
        if delta[delta_c] != '':    # костыль исключает первое расстояние = 0
            dr.text((offset + int(delta[delta_c]) * step // 200 - text_size * 0.3 * len(delta[delta_c]),
                     im.height - 25 * scale_a5), delta[delta_c], font=font, fill=1)
            dr.text((offset + int(delta[delta_c]) * step // 200 - text_size * 0.3 * len(delta[delta_c]),
                     im.height - 73 * scale_a5), delta[delta_c], font=font, fill=1)
        delta_c += 1

        if h_len[1] != 0:   # для промежуточных точек
            offset = step * step_count + offset_corner + step / 100 * h_len[1]
        else:
            step_count += 1
            offset = step * step_count + offset_corner

        x_of_point.append(offset)
        dr.line((offset, im.height - 29 * scale_a5, offset, im.height - 17 * scale_a5), fill=1)
        dr.line((offset, im.height - 77 * scale_a5, offset, im.height - 65 * scale_a5), fill=1)
        dr.text((offset - scale_a5, bottom - 8 * scale_a5), name, font=font, fill=1)
        txt = Image.new(mode='RGB', size=(text_size * len(str(h_len[0])) // 2, text_size), color=(255, 255, 255))
        txt_dr = ImageDraw.Draw(txt)
        txt_dr.text((0, 0), str(h_len[0]), font=font, fill=1)
        txt = txt.rotate(90, expand=True)
        x, y = int(offset - scale_a5 * 2), int(im.height - 39.5 * scale_a5)
        lx, ly = txt.size
        im.paste(txt, (x, y, x + lx, y + ly))

    horizon = usl_horizon(pickets)
    spec = [i[0] for i in pickets.values()]     # все высоты
    fx = x_of_point[0]
    fy = usl_horizon_line - (spec[0] - horizon) * scale_y * 1000 * scale_a5

    for ind, i in enumerate(spec[1:]):
        dr.line((fx, fy, x_of_point[ind + 1], usl_horizon_line - (i - horizon) * scale_y * 1000 * scale_a5),
                fill=1, width=int(scale_a5/2))
        fx = x_of_point[ind + 1]
        fy = usl_horizon_line - (i - horizon) * scale_y * 1000 * scale_a5
        dr.line((fx, fy, fx, usl_horizon_line), fill=1)

    # получаем данные для построения трассы
    trail = calc.volume_algo(pickets)[:2]
    work = calc.volume_algo(pickets)[2:4]
    proj = calc.volume_algo(pickets)[4:]
    fx = x_of_point[0]
    fy = usl_horizon_line - (spec[0] - horizon) * scale_y * 1000 * scale_a5
    const_x = fx

    # отрисовка трассы
    for i in trail:
        dr.line((fx, fy, i[1] * scale_a5 * scale_x * 1000 + const_x,
                 usl_horizon_line - (i[0] - horizon) * scale_y * 1000 * scale_a5), fill='red', width=int(scale_a5/2))
        fy = usl_horizon_line - (i[0] - horizon) * scale_y * 1000 * scale_a5
        fx += i[1] * scale_a5 * scale_x * 1000

    # отрисовка рабочих отметок
    st = const_x
    for ix, i in enumerate(work):
        for j in i:
            delta_rab = list(map(int, delta[1:]))
            if ix == 1:
                delta_rab = delta_rab[len(delta_rab) // 2:]
            num = round(j, 2)
            while num > 0:
                num -= delta_rab[0]
                delta_rab = delta_rab[1:]
            num = round(abs(num), 2)
            txt_x = j * scale_a5 * scale_x * 1000 + st
            txt_y = bottom - 12 * 6 * scale_a5
            # dr.text((txt_x + scale_a5 * 2, txt_y - text_size), fill='blue', font=font, text=str(num)) # horisontal
            # vertical
            txt = Image.new(mode='RGB', size=(text_size * len(str(num)) // 2, text_size), color=(255, 255, 255))
            txt_dr = ImageDraw.Draw(txt)
            txt_dr.text((0, 0), str(num), font=font, fill='blue')
            txt = txt.rotate(90, expand=True)
            x, y = int(txt_x + text_size // 2), int(txt_y - 10 * scale_a5)
            lx, ly = txt.size
            im.paste(txt, (x, y, x + lx, y + ly))
            dr.line((txt_x, txt_y, txt_x, usl_horizon_line - (trail[ix][2] * j + trail[ix][3] - horizon)
                     * scale_a5 * scale_y * 1000), fill='blue')
        st += trail[0][1] * scale_a5 * scale_x * 1000

    # отрисовка уклонов
    red_x = x_of_point[0]
    delta_xs = trail[0][1], trail[1][1] - trail[0][1]
    for i in range(2):
        prom = str(round(trail[i][2] * 1000, 2))
        len_line = str(delta_xs[i])
        if trail[i][2] > 0:     # если уклон положительный
            red_y = usl_horizon_line + 12 * 3 * scale_a5
            delta_x = delta_xs[i] * scale_a5 * scale_x * 1000
            dr.line((red_x, red_y, red_x + delta_x, red_y - 12 * scale_a5), fill='red')
            dr.text((red_x + delta_x - len(len_line) * text_size, red_y - text_size * 2),
                    text=len_line, font=font, fill='red')
            dr.text((red_x + len(prom) * text_size, red_y - text_size * 2),
                    text=prom, font=font, fill='red')
            red_x += delta_x
            dr.line((red_x, red_y, red_x, red_y - 12 * scale_a5), fill=1)
        else:   # если уклон отрицательный
            red_y = usl_horizon_line + 12 * 2 * scale_a5
            delta_x = delta_xs[i] * scale_a5 * scale_x * 1000
            dr.line((red_x, red_y, red_x + delta_x, red_y + 12 * scale_a5), fill='red')
            dr.text((red_x + delta_x - len(prom) * text_size, red_y - text_size * 2 + 12 * scale_a5),
                    text=prom, font=font, fill='red')
            dr.text((red_x + len(len_line) * text_size, red_y - text_size * 2 + 12 * scale_a5),
                    text=len_line, font=font, fill='red')
            red_x += delta_x
            dr.line((red_x, red_y, red_x,red_y + 12 * scale_a5), fill=1)

    # отрисовка проектных отметок
    first_h = spec[0]
    txt = Image.new(mode='RGB', size=(text_size * len(str(first_h)) // 2, text_size), color=(255, 255, 255))
    txt_dr = ImageDraw.Draw(txt)
    txt_dr.text((0, 0), str(first_h), font=font, fill='red')
    txt = txt.rotate(90, expand=True)
    x, y = int(offset_corner - scale_a5 * 2), int(im.height - 63.5 * scale_a5)
    lx, ly = txt.size
    im.paste(txt, (x, y, x + lx, y + ly))
    x_of_proj = x_of_point[1:]
    x_count = 0

    for mas in proj:
        mas = mas[:2]
        for i, d_x in zip(mas[0], mas[1]):
            txt = Image.new(mode='RGB', size=(text_size * len(str(i)) // 2, text_size), color=(255, 255, 255))
            txt_dr = ImageDraw.Draw(txt)
            txt_dr.text((0, 0), str(i), font=font, fill='red')
            txt = txt.rotate(90, expand=True)
            x, y = int(x_of_proj[x_count] - scale_a5 * 2), int(im.height - 63.5 * scale_a5)
            x_count += 1
            lx, ly = txt.size
            im.paste(txt, (x, y, x + lx, y + ly))

    im.show()
    im.save(f'{profile_name}.png')

# pickets_data = excel_pars.find_pickets()
# draw_profile(pickets_data)
#draw_profile(m_x_scale=2000, m_y_scale=200, profile_name='f')