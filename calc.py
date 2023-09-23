import excel_pars
pickets = excel_pars.find_pickets()
def kx_find(pic, delta):
    save_fun = []
    st = pic[0][0]
    for ind, j in enumerate(pic[1:]):
        dh = j[0] - st
        k = dh / delta[ind]
        st = j[0]
        save_fun.append(round(k, 4))
    return save_fun

def min_work(kx, delta, range_of_h, h):
    print(kx, delta, range_of_h, h)
    vol_mas = []
    for i in range(1, range_of_h + 1):
        kf = round((min(h) + 0.05 * i - h[0]) / sum(delta), 4)
        #print(kf)
        volume = 0
        current_x = 0
        for ind_k, j in enumerate(delta):
            prev_x = current_x
            current_x += j
            int1 = abs(kf * current_x ** 2 / 2 + h[0] * current_x - kf * prev_x ** 2 / 2 - h[0] * prev_x)
            #int2 = kx[ind_k] * current_x ** 2 / 2 + h[ind_k] * current_x - (kx[ind_k] * prev_x ** 2 / 2 + h[ind_k] * prev_x)
            int_2trap = abs((h[ind_k] + h[ind_k + 1]) / 2 * j)
            volume += int1 - int_2trap

        vol_mas.append((abs(volume), 0.05 * i))
        print(volume)
    return min(vol_mas)
def delta_f(pic_len):
    first = pic_len[0][1]
    delta = []
    for i in pic_len[1:]:
        sec = i[1]
        if i[1] == 0:
            sec = 100
        delta.append(sec - first)
        first = i[1]
    return delta

def volume_algo(pickets):
    no_name = [list(i) for i in pickets.values()]
    f_half = no_name[:len(no_name) // 2 + 1]
    s_half = no_name[len(no_name) // 2:]
    delta1 = delta_f(f_half)
    delta2 = delta_f(s_half)
    kx1 = kx_find(f_half, delta1)
    kx2 = kx_find(s_half, delta2)
    h1 = list(map(lambda x: x[0], f_half))
    range_of_h1 = int((max(h1) - min(h1)) / 0.05)
    data1 = min_work(kx1, delta1, range_of_h1, h1)
    s_half_mod = s_half.copy()
    s_half_mod[0][0] = data1[1] + h1[0]
    h2 = list(map(lambda x: x[0], s_half_mod))
    range_of_h2 = int((max(h2) - min(h2)) / 0.05)
    data2 = min_work(kx2, delta2, range_of_h2, h2)
    f_connect, s_connect = (min(h1) + data1[1], sum(delta1)), (min(h2) + data2[1], sum(delta1 + delta2))
    return f_connect, s_connect

print(volume_algo(pickets))