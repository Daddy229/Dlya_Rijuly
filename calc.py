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
for i in range(1, range_of_h + 1):
    kf = 0.05 * i / sum(delta)
    print(0.05 * i + h[0])
    volume = 0
    for indk, j in enumerate(delta):
        volume += (kf * j ** 2 / 2 + h[0] * j - (all_kx[indk] * j ** 2 / 2 + h[indk] * j)) * -1
    print(volume)


