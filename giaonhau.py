a,b=eval(input('nhap a va b '))
c,d=eval(input('nhap khoang c va d'))
l=p=k=[]
if a>d or b<c:print('khong giao')
else:
 for i in range(a,b+1):
    l=l+[i]
 for i in range(c,d+1):
    p=p+[i]
 for i in l:
    if i in p:k=k+[i]
print(k)