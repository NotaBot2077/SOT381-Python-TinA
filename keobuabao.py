p1=input('nhap su lua chon cua nguoi choi 1 ')
p2=input('nhap su lua chon cua nguoi choi 2 ')
if p1!=p2:
 if p1=='bua':
  if p2=='keo':print('nguoi choi 1 thang')
  else:print('nguoi choi 2 thang')
 elif p1=='keo':
  if p2=='bao':print('nguoi choi 1 thang')
  else:print('nguoi choi 2 thang')
 else:
     if p2=='bua':print('nguoi choi 1 thang')
     else:print('nguoi choi 2 thang')
else:
    print('hoa')