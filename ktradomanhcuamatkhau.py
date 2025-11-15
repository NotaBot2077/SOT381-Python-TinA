password=input('nhap mat khau')
if len(password)>=8:
  if len(password)>=12:print('mat khau manh')
  else:print('mat khau trung binh')
else:print('mat khau yeu')