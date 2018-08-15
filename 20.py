
if __name__ == '__main__':
    n=int(input('input down times(>=1):'))
    sumx=0
    
    for i in range(1,n+1):
        last=100/pow(2,i-1)
        if i==1:
            sumx=100
        else:
            sumx+=last*2

    print('all miters passed is :%f'% sumx)
