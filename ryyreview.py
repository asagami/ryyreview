from functools import wraps
import datetime

def log(func):
    @wraps(func)
    def wrapper (*args,**kwargs):
        print(func.__name__,'\n',datetime.datetime.now())
        return func(*args,**kwargs)
    return wrapper



class Student(object):
    def __init__(self,name,number,score):
        self.__name=name
        self.__number=number
        self.__score=score

    def setname(self,name):
        if isinstance(name,int):
            raise ValueError("string is illegal")
        if len(name)>10:
            raise ValueError("name to long")
        self.__name=name

    def getname(self):
        return self.__name

    def getnumber(self):
        return self.__number

    def getscore(self):
        return self.__score

    def PrintList(self):
        List=[]
        for i in range(1,10):
            List.append(i)
        print(List);

    def ReverseString(self):
        List=[]
        a="i have a problem"
        for i in a:
            List.append(i)
        List.reverse();
        print(''.join(List))


class GoodStudent(Student):
    def __init__(self,*args):
        super().__init__(*args[:3])
        self.__status=args[-1]

    def getstatus(self):
        return self.__status


    @log
    def setstatus(self,status):
        self.CheckStatus(status)
        self.__status=status
        'efqef'.join('')[::-1]


    def CheckStatus(self,status):
        if not isinstance(status,int):
            raise ValueError("TYPE IS NOT LEGAL")
        if status>15:
            raise ValueError("too long")






