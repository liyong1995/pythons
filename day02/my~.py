if __name__ == '__main__':
    nset = {1,2,3,4,5,6}
    print(type(nset))


    a = input("请输入字符串：")
    mset = set(a)
    print(a.__len__())
    print(mset.__len__())
    if a.__len__()>mset.__len__() :
        print("有重复")
    else :
        print("无重复")
