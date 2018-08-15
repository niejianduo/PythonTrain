if __name__ == '__main__':

    for n in range(1,1000):
        f=[]
        sumn=0
        for i in range(1,int(n/2)+1):
            if n%i==0 :
                f.append(i)
        for j in range(0,len(f)):
            sumn+=f[j]
        if sumn==n:
            print('%3d = %3d'%(sumn,f[0]),end='')
            for k in range(1,len(f)):
                print(' + %3d' % f[k],end='')
            print('')
        
