salary=int(input('nhap thua nhap tong thu hang thang(don vi:nghin dong)'))
tax=0
if salary>0:
  if salary <=5000:tax=5
  else:tax =10
else:tax=0
print('thu nhap sau thue la',(salary-tax))