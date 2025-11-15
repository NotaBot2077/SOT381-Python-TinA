donhang=input('chon loai giao han ma ban muon ')
cannang=float(input('nhap can nang don hang(don vi:kg):'))
khoangcach=float(input('nhap khoang cach(don vi:km):'))
if donhang=='tieu chuan':
    basefee=25
    if cannang>2:basefee=basefee+(cannang-2)*5
    if khoangcach>30:basefee=basefee+15
    print(basefee)
else:
    basefee=50
    if cannang>1:basefee=basefee+(cannang-1)*10
    if khoangcach>10:basefee=basefee+20
    print(basefee)