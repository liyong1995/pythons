if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    # 1.编写Python程序判断字符串是否重复。
    nlist = [i.strip() for i in klist]
    klen = len(klist)
    nlen = len(nlist)
    if klen == nlen :
        print("无重复")
    else :
        print("有重复")
    # 2.编写Python程序打印输出字符串中重复的所有字符。
    nset = set(nlist)

    for i in nset :
        num = nlist.count(i)
        if num > 1 :
            print(i)


    # 3.把下面的klist作为字典的键,同时作为字典的值
    ndict = {i:i for i in nset}
    print(ndict)

    # 4.  把下面的klist作为字典的键,并统计每个单词的词频
    mdict = {}
    for i in nset :
        mdict[i] = nlist.count(i)
    print(mdict)