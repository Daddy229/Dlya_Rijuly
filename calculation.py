from openpyxl import load_workbook

# open
name = 'test.xlsx'
file = load_workbook(name)
sheet = file.active
sheet.clear()
# заполняем шапку
line1 = ['№ станции', 'Точка визирования', 'остчёты по рейкам', '', '', 'Превышения', '', 'Горизонт прибора', 'Высота']
line2 = ['', '', 'задний', 'передний', 'промежуточный', 'h', 'hcp']     # 2 space
start = ord('A')

file.save(name)
file.close()