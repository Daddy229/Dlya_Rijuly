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
    vol_mas = []
    for i in range(-range_of_h, range_of_h + 1):
        kf = round((h[-1] + 0.05 * i - h[0]) / sum(delta), 4)
        #print(kf)
        volume = 0
        current_x = 0
        for ind_k, j in enumerate(delta):
            prev_x = current_x
            current_x += j
            int1 = abs(kf * current_x ** 2 / 2 + h[0] * current_x - kf * prev_x ** 2 / 2 - h[0] * prev_x)
            #int2 = kx[ind_k] * current_x ** 2 / 2 + h[ind_k] * current_x - (kx[ind_k] * prev_x ** 2 / 2 + h[ind_k] * prev_x)   # suka piton dayn
            int_2trap = abs((h[ind_k] + h[ind_k + 1]) / 2 * j)
            volume += int1 - int_2trap

        vol_mas.append((abs(volume), 0.05 * i, kf))
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

def work_marks(data, kx, h, delta):
    kf = data[2]
    range_x = list(range(1, sum(delta) + 1))
    cur_x = 0
    marks = []
    for ix, i in enumerate(kx):
        if kf == kx[ix]:
            continue
        x = (h[ix] - cur_x * kx[ix] - h[0])/(kf - kx[ix])
        cur_x += delta[ix]
        if int(x) in range_x:
            marks.append(x)
    return marks

def project_points(kf, delta, h):
    points = []
    cur_x = 0
    for i in delta:
        cur_x += i
        hight = h + kf * cur_x
        points.append(round(hight, 2))
    return points, delta, h
def volume_algo(pickets):
    no_name = [list(i) for i in pickets.values()]
    f_half = no_name[:len(no_name) // 2 + 1]
    s_half = no_name[len(no_name) // 2:]
    delta1 = delta_f(f_half)
    delta2 = delta_f(s_half)
    kx1 = kx_find(f_half, delta1)
    kx2 = kx_find(s_half, delta2)
    h1 = list(map(lambda x: x[0], f_half))
    range_of_h1 = int(h1[-1] / 0.05)
    data1 = min_work(kx1, delta1, range_of_h1, h1)
    h1[-1] = h1[-1] + data1[1]
    s_half_mod = s_half.copy()
    s_half_mod[0][0] = h1[-1]
    h2 = list(map(lambda x: x[0], s_half_mod))
    range_of_h2 = int(h2[-1] / 0.05)
    data2 = min_work(kx2, delta2, range_of_h2, h2)
    # меняю минимум на последнюю
    f_connect, s_connect = (h1[-1], sum(delta1), data1[-1], h1[0]),\
        (h2[-1] + data2[1], sum(delta1 + delta2), data2[-1], h2[0])
    rab_otm1 = work_marks(f_connect, kx1, h1, delta1)
    rab_otm2 = work_marks(s_connect, kx2, h2, delta2)
    proj1 = project_points(data1[2], delta1, h1[0])
    proj2 = project_points(data2[2], delta2, h2[0])
    return f_connect, s_connect, rab_otm1, rab_otm2, proj1, proj2

a = volume_algo(pickets)
#work_marks(a[0], )