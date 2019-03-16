if __name__ == '__main__':
    a1 = "asdasdasd"
    i=0
    for j in a :
        num = a.count(j)
        print(num)
        if num>1 :
            print(j)

    yset = set(a1)
    print(yset)

    mset = {"a","b","c",1,2,3}
    print(mset)
    a = [i for i in mset]
    print(a)

    str = input("请输入一个字符串：")
    mset = set(str)
    mlist = [i for i in mset]
    for i in mlist :
        num = str.count(i)
        if num>1 :
            print(str(i)+"重复次数"+str(num))


    mlist = ["bbb","ccc","aaa"]
    nlist = ["aaa","bbb","ccc","aaa"]

    ndict = {}
    for i in mlist :
        ndict[i] = nlist.count(i)
    print(ndict)
    mdict = sorted(ndict)
    print(mdict)

    mlist = ["name","age","password"]
    nlist = [1,2,3]
    ndict = {}


    ndict = {k:v for k in mlist for v in nlist}


    ndict.update(mlist, nlist)

    print(ndict)


