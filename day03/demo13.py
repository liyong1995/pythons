if __name__ == '__main__':


    m1 = int(input("请输入第一个月份："))
    m2 = int(input("请输入第二个月份："))

    if m1>m2 :
        n = m1 % m2
    else :
        n = m2%m1
    if n == 1 :
        print("非常有缘")
    elif n == 2 :
        print("比较有缘")
    elif n == 3:
        print("缘分一般")
    elif n == 4:
        print("有仇")
    else :
        print("无缘分")
