if __name__ == '__main__':
    str = input("请输入一个字符串：")
    nset = set(str)

    slen = len(str)
    nlen = len(nset)
    print(slen,nlen)
    if slen == nlen :
        print("无重复")
    else :
        print("有重复")

