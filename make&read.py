# подключаем библиотеки
from openpyxl import load_workbook
from openpyxl.styles import Alignment

# проверка пикета
sign = '+-1234567890'

# открываем файл
name = 'test.xlsx'
file = load_workbook(name)
sheet = file.active

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
        for j in range(3, 29):
            sheet[f'{chr(start)}{j}'].alignment = Alignment(horizontal='center')
        start += 1
    file.save(name)

def read_info():
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
        print(line)
    print(dic)

make_title()
read_info()
file.close()