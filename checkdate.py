day=int(input("nhap ngay "))
month=int(input("nhap thang "))
year=int(input("nhap nam "))
print(day,month,year,sep='/')
if day>=1 and day<=31 and month>=1 and month<=12:
   if year%4==0 and year%100!=0:
      if month==4 or month==9 or month==11 or month==6 and  day <=30:print('true')
      elif month==1 or month==3 or month==5 or month==7 or month==8 or month ==12 and  day <=31:print('true')
      elif month==2:
           if day<=29:print("true")
           else:print('false')
      else:print('false')
   else:
    if month==4 or month==9 or month==11 or month==6 and  day <=30:print('true')
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month ==12 and  day <=31:print('true')
    elif month==2:
           if day<=28:print("true")
           else:print('false')
    else:print('false')
else:
  print("false")
