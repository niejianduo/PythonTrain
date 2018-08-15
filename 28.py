def old(n):
    if n==1:
        return 10
    else:
        return 2+old(n-1)

if __name__=='__main__':
    n=5
    age=old(n)
    print(age)
