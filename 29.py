import re

class CustomError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo

if __name__=='__main__':

    while True:
        number = input("Please input the number:")
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
                if n>=10000:
                    print(n)
                    raise CustomError('Exception')
                if n//1000 !=0:
                    print("这个数是%d位数" % 4)
                    print('从高到低位数字分别是: ',n//1000,(n//100)%10,(n%100)//10,n%10)
                elif n//100 !=0:
                    print("这个数是%d位数" % 3)
                    print('从高到低位数字分别是: ',n//100,(n//10)%10,n%10)
                elif n//10 !=0:
                    print("这个数是%d位数" % 2)
                    print('从高到低位数字分别是: ',n//10,n%10)
                else:
                    print("这个数是%d位数" % 1)
                    print('从高到低位数字分别是: ',n)
        except CustomError as e:
            print(e)
#       else:

#       finally:
         
    
