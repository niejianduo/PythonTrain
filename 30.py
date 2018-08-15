import re

class CustomError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo

if __name__=='__main__':
    for n in range(10000,100000):
        if n//10000 == n%10 and (n//1000)%10 ==(n%100)//10:
            print(n,' 是回文数')
        '''
    while True:

        number = input("Please input the number(10000-99999):")
        #print(type(number))
        try:   
            #调用正则
            value = re.compile(r'^[-+]?[0-9]+[0-9]*$')
            result = value.match(number)
        
            if not result:
                print(result)
                raise CustomError('Exception')
            else:
                n=int(number)
                if n>=100000 or n<10000:
                    print(n)
                    raise CustomError('Exception')
                if n//10000 == n%10 and (n//1000)%10 ==(n%100)//10:
                    print(n,' 是回文数')
                else:
                    print('这个数字不是回文数')

        except CustomError as e:
            print(e)
        '''
#       else:

#       finally:


    
