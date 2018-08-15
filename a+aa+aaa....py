

if __name__ == '__main__':
 while True:
    n=int(input("input number:"))
    num=n
    f=[]
    for i in range(2,n):
        for j in range(2,int(n/2)+1):
            if n%j ==0:
                f.append(j)
                n=n//j
                break

    if len(f)==0:
        print('该数字没有任何质因子')
    else:
        f.append(n)
        f.reverse()
        print('%d = %d' % (num,f[0]),end='')
        for k in range(1,len(f)):
              print('*%d' % f[k],end='')
    print('')
                
