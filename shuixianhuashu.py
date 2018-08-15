

if __name__ == '__main__':
    x=int(input("how many numbers:"))
    y=input('what number:')
    tem=''
    sumnum=0
    for i in range(0,x):
        tem=tem+y
        sumnum+=int(tem)
    print(sumnum)
        
                
