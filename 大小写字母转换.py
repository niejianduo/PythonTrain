    def aplusb(self, a, b):
        # write your code here
        return (a+b)
    
    def main():
        a1=int(input('input first number:'))
        b1=int(input('input second number:'))
        sumab=aplusb(a1,b1)
        print('sum of a b is:',sumab)
    if __name__ == '__main__':
        main()