n=input('nhap phong')
day=int(input('nhap ngay '))
if n=='Standard':
  if day>3:
    print('gia ve la',1000000*day*0.9)
  else:
    print('gia ve la ',1000000*day)
elif n=='Deluxe':
   if day>3:
    print('gia ve la',1500000*day*0.9)
   else:
    print('gia ve la ',1500000*day)
else:
  if day>3:
    print('gia ve la',2500000*day*0.9)
  else:
    print('gia ve la ',2500000*day)