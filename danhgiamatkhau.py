password=input('nhap mat khau')
point=0
n=m=p=[]
if len(password)>=8:point=point+1
if len(password)>=12:point=point+1
for i in password:
    if '1'<=i<='9':n=n+[i]
    if "A"<=i<="Z":m=m+[i]
    if i in "!@#$%^&*()-_=+[]{};:'\",.<>?/":p=p+[i]
if len(m)!=0:point=point+1
if len(p)!=0:point=point+1
if len(n)!=0:point=point+1
print(point)
if point==5:print('mat khau rat manh')
else:
  if point>=3:print('mat khau manh')
  else:
    if point<2:print('mat khau yeu')
    else:print('mat khau trung binh')