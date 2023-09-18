# подключаем библиотеки
from openpyxl import load_workbook
from openpyxl.styles import Alignment

# открываем файл
name = 'test.xlsx'
file = load_workbook(name)
sheet = file.active

# заполняем шапку
line1 = ['№ станции', 'Точка визирования', '', 'остчёты по рейкам', '', 'Превышения', '', 'Горизонт прибора', 'Высота']
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
file.save(name)
file.close()