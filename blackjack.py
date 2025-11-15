card1=input('nhap bai 1 ')
card2=input('nhap bai 2 ')
card3=input('nhap bai 3 ')
sumcard=0
def check(j):
    sumcar=0
    numace=0
    for la in j:
     if la in ["J","Q","K"]:
        sumcar=+10
     elif la=="A":
        sumcar=+11
        numace=numace+1
     else:
        sumcar=sumcar+int(la)
    while sumcar>21 and numace>0:
        sumcar=sumcar-10
        numace=numace-1
    return sumcar
print(check([card1,card2,card3]))