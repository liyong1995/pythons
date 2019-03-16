if __name__ == '__main__':
    # 定义一个变量，用于接收输入的数字
    num = int(input("请输入一个数字："))
    i=1;

    while i<=num :
        j=1
        k=1

        while k<=num-i :
            print(" ",end=" ")
            k += 1
        while j<=(2*i)-1 :
            print("*",end=" ")
            j += 1
        print()
        i += 1
    i = num
    while i >= 1:
        j = 2
        k = num

        while k >= i:
            print(" ", end=" ")
            k -= 1
        while j < (2 * i) - 1:
            print("*", end=" ")
            j += 1
        print()
        i -= 1