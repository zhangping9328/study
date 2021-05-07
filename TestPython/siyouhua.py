class Test(object):
    def __init__(self):
        self.__num = 100
  #      self.num = 100
    def setNum(self,Num):
        self.__num = Num
        return self.__num
    def getNum(self):
        return self.__num



t = Test()
#t.__num 有2种理解 添加一个变量，修改一个变量，因为是私有变量所以无法修改，添加
#t.__N = 201
# t.g = 1
# print(t.g)
print(t.getNum())
t.setNum(5)
print(t.setNum(5))