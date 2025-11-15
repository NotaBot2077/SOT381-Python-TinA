ticket=input("nhap xe ")
hour=input("nhap gio ")
def lamtron(hour):
 c=hour.find('.')
 a="0"+hour[c:]
 b=float(hour)
 h=float(a)
 if h>= 0.5:
     return int(b-h+1)
 else:
     return int(b-h)
print(lamtron(hour))
if ticket=="xe may":
    if lamtron(hour)<=2:print("5k")
    else:print(5+(lamtron(hour)-2)*2,"k")
else:
    if lamtron(hour)<=1:print("20k")
    else:print(20+(lamtron(hour)-1)*15,"k")