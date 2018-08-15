

if __name__ == '__main__':
  while True:
    a=b=c=0
    n=input("input string:")
    n.split()
    for i in range(0,len(n)):
        if n[i].isdigit():
            a+=1
        elif n[i].isalpha():
            b+=1
        else:
            c+=1
    print('digit number is: %d' % a)
    print('letter number is: %d' % b)
    print('other char number is: %d' % c)
        

                
