if __name__ == '__main__':
    mdict = {'c':1,'b':2,'a':3}
    print(mdict)

    print(mdict['b'])
    print("{0}={1}".format('b',mdict['b']))

    nlist = ["name","password","age"]
    ndict = {}
    for k in nlist :
        ndict.setdefault(k)
    print(ndict)

    val = str(ndict)
    print("a"+val)
    print(str(ndict))

    print(len(ndict))

    a = mdict.get('b')
    print(a)

    for k in mdict.keys() :
        print(k)
    for v in mdict.values() :
        print(v)
    for i in mdict :
        print(i)

    mmdict = sorted(mdict)
    print(mmdict)
