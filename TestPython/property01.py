class testProperty(object):
    #__num 是私有变量
    def __init__(self):
        self.__num = 100
    def setNum(self,newNum):
        print("----------1----------")
        self.__num = newNum
    def getNum(self):
        print("----------2----------")
        return self.__num
    num = property(getNum,setNum)
t = testProperty()
t.num = 300
print(t.num)


# t.num = 300 相当于直接调用 t.setNum(300)
# t.num 相当于调用 t.getNum()
# t.num 到底是调用t.setNum()还是调用t.setNum()要根据实际场景判断
# 如果是给 t.num 赋值肯定是调用 t.setNum()
# 如果是获取 t.num 肯定是调用 t.getNum()
#property的作用：相当于对方法进行了封装，开发者对属性的更新更方便了
