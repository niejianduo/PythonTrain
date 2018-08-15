def multip(n):
    if n==1:
        return 1
    else:
        return n*multip(n-1)

if __name__=='__main__':
  while True:
    n=int(input('请输入要求和的项数:'))
    sums=0
    for i in range(1,n+1):
        print(multip(i),' ',end='')
        sums+=multip(i)
    print('')
    print(sums)
    
