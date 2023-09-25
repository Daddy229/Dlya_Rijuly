# подключаем библиотеки
from openpyxl import load_workbook
from openpyxl.styles import Alignment

# проверка пикета
sign = '+-1234567890'

# открываем файл
name = 'test.xlsx'
file = load_workbook(name)
sheet = file['lst']

# заполняем шапку
def make_title():
    line1 = ['№ станции', 'Точка визирования', '', 'остчёты по рейкам',
             '', 'Превышения', '', 'Горизонт прибора', 'Высота']
    line2 = ['', '', 'задний', 'передний', 'промежуточный', 'h', 'hcp']
    start = ord('A')    # это для букав

    for i in range(len(line1)):
        sheet[f'{chr(start)}1'] = line1[i]
        sheet.column_dimensions[f'{chr(start)}'].width = 18
        sheet[f'{chr(start)}1'].alignment = Alignment(horizontal='center')
        start += 1

    start = ord('A')

    for i in range(len(line2)):
        sheet[f'{chr(start)}2'] = line2[i]
        sheet[f'{chr(start)}2'].alignment = Alignment(horizontal='center')
        start += 1

    start = ord('A')

    for i in range(len(line1)):
        for j in range(3, 329):
            sheet[f'{chr(start)}{j}'].alignment = Alignment(horizontal='center')
        start += 1
    file.save(name)

def clear_table():
    start = ord('A')
    for i in range(100):
        for j in range(9):
            sheet[f'{chr(start + j)}{3 + i}'] = ''
    file.save(name)

def read_info(only_read=False):
    threshold = 0
    line = 3
    dic = {}
    spis = []
    s = ord('A')
    while True:
        for i in range(9):
            spis.append(sheet[f'{chr(s)}{line}'].value)
            s += 1
        if not list(filter(lambda x: not(x is None), spis)):
            threshold += 1
            if threshold == 3:
                break
        else:
            threshold = 0
        dic.setdefault(line, spis.copy())
        spis.clear()
        s = ord('A')
        line += 1
    first = True
    if only_read:
        return dic

    int_point = 0   # чтобы не ругался (забей) и так ещё две строки
    horizon = 0
    int_points = []
    for k, v in dic.items():
        if not(v[0] is None):
            int_points = []
            h_black = v[2] - dic[k + 1][3]
            h_red = dic[k + 1][2] - dic[k + 2][3]
            r_pyatok1 = dic[k + 1][2] - v[2]
            r_pyatok2 = dic[k + 2][3] - dic[k + 1][3]
            sheet[f'C{k + 2}'] = r_pyatok1
            sheet[f'D{k + 3}'] = r_pyatok2
            up_mean = (h_red + h_black) / 2
            sheet[f'F{k + 1}'] = h_black
            sheet[f'F{k + 2}'] = h_red
            sheet[f'G{k + 1}'] = round(up_mean)
            if not first:
                sheet[f'I{k}'] = int_point
                dic[k][-1] = int_point
            horizon = v[2] + v[-1] * 1000
            sheet[f'H{k}'] = horizon
            sheet[f'I{k+1}'] = round((v[-1] * 1000 + up_mean) / 1000, 3)
            dic[k+1][-1] = round((v[-1] * 1000 + up_mean) / 1000, 3)
            int_point = dic[k + 1][-1]
            int_points.append(dic[k][1])
            int_points.append(dic[k + 1][1])
            first = False
        if v[1] not in int_points and not(v[1] is None):
            v[-1] = horizon - v[4]
            sheet[f'I{k}'] = round(v[-1] / 1000, 3)
    file.save(name)
    return dic

def find_pickets():
    dic = read_info(only_read=True)
    rasst_dic = {}
    last_picket = 'None'
    for k, v in dic.items():
        if isinstance(v[1], str):
            rasst_dic.setdefault(v[1], (round(v[-1], 2), 0))
            last_picket = v[1]
        if isinstance(v[1], int):
            rasst_dic.setdefault(f'+{v[1]}', (round(v[-1], 2), v[1]))
    return rasst_dic

file.close()