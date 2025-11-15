workhour=int(input('nhap so gio lam viec '))
payperhour=int(input('nhap muc luong moi gio '))
if workhour<=40:print('thu nhap la ',workhour*payperhour)
else:print('thu nhap la ',workhour*payperhour+(workhour-40)*payperhour*1.5)