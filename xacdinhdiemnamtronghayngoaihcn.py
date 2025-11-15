x1,y1=eval(input('nhap toa do go tren '))
x2,y2=eval(input('nhap toa do go duoi '))
x,y=eval(input('nhap toa do diem '))
if x1<x<x2 and y2<y<y1:print('trong hinh chu nhat')
elif x==x1 or x==x2 and y2<y<y1:print('nam tren canh')
elif y==y1 or y==y2 and x1<x<x2:print('nam tren canh')
else:
    print('nam ngoai')