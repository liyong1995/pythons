if __name__ == '__main__':
    num = int(input("请输入一个数字："))
    a = []
    while 1 == 1:
        c = num % 2
        a.insert(0, str(c))
        num = num // 2
        if num <= 0:
            break
    b = ""
    for i in a:
        b += str(i)
    print(b)

    print(a)
    print("".join(a))