import excel_pars

pickets = excel_pars.find_pickets()
delta = []
pic_len = list(pickets.values())
first = pic_len[0][1]
h = list(map(lambda x: x[0], pic_len))
range_of_h = int((max(h) - min(h)) / 0.05)
print(range_of_h, h)

for i in pic_len[1:]:
    sec = i[1]
    if i[1] == 0:
        sec = 100
    delta.append(sec - first)
    first = i[1]
print(delta)
def kx_find(pic):
    save_fun = []
    st = pic[0][0]
    for ind, j in enumerate(pic[1:]):
        dh = j[0] - st
        k = dh / delta[ind]
        st = j[0]
        save_fun.append(k)
    return save_fun

all_kx = kx_find(pic_len)
print(all_kx)
vol_mas = []
for i in range(1, range_of_h + 1):
    kf = 0.05 * i / sum(delta)
    volume = 0
    curent_x = 0
    for indk, j in enumerate(delta):
        prev_x = curent_x
        curent_x += j
        volume += (kf * curent_x ** 2 / 2 + h[0] * curent_x - kf * prev_x ** 2 / 2 - h[0] * prev_x) - (
                all_kx[indk] * curent_x ** 2 / 2 + h[indk] * curent_x - all_kx[indk] * prev_x ** 2 - h[indk] * prev_x)
    vol_mas.append((abs(volume), kf, 0.05 * i))

print(*vol_mas, sep='\n')
