def louti():
    for i in range(50,1,-1):
        for j in range(1,i+1):
            if(j!=i):
                print("M",end='')
            else:
                print('')

if __name__ == '__main__':
    louti()
    
