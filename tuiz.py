
if __name__ == '__main__':
    symbol=1
    for i in range(101,201):
        for j in range(2,int((i+1)/2)):
            if i%j==0:
                symbol=0;
                break
            else:
                symbol=1;
        if symbol:
                print(i)
                
