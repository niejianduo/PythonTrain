def fenzi(down):
    if down==1:
        return 2
    elif down==2:
        return 3
    else:
        return fenzi(down-2)+fenzi(down-1)
    
def fenmu(up):
    if up==1:
        return 1
    elif up==2:
        return 2
    else:
        return fenmu(up-1)+fenmu(up-2)

while True:
    n=int(input('请输入求和的数列项数：')) 
    sums=0

    for i in range(1,n+1):
        a=fenzi(i)
        b=fenmu(i)
        sums+=a/b
        print(a,'/',b)
    print(sums)

