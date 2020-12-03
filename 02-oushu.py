#打印0-100的偶数，计算偶数奇数的个数
i = 0
sum = 0
while i<=100:
    if i %2 ==0:
        sum+=1
        print(i)
    if sum ==20:
        print("偶数的个数是：%d" % sum)
        break


    i+=1