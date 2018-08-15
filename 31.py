import re

class CustomError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo

if __name__=='__main__':

    while True:
        week='Monday tuesday wensday thursday friday saturday sunday'
        number = input("请输入星期的字母:")
        try:   
            #调用正则
            bt='('+number+'\w+'+')'
            print(bt)
            value = re.findall(bt,week,re.I)
            #print(value)
            
            if not value:
                raise CustomError('No this day')
            else:
                print('This is:',value)

        except CustomError as e:
            print(e)

#       else:

#       finally:


    
