if __name__ == '__main__':
    str = input("请输入一个字符串：")

    nset = set(str)

    for i in nset :
        num = str.count(i)
        if num >1 :
            print(i)

    nlist = list(nset)

    print(type(nlist))

    ndict = {}
    for i in sorted(nlist) :
        ndict[i] = str.count(i)
    print(ndict)






