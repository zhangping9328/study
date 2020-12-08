#内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包。

def straight_line(a,b):
    def line(x):
        y = a*x+b
        return y
    return line
line1 = straight_line(4,5)

print(line1(1))
