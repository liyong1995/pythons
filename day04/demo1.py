if __name__ == '__main__':
    mfile = open(r"a.c")
    # 判断文件的可读性
    flag = mfile.readable()
    print(flag)

    #读取全部文件内容
    val = mfile.read()
    print(val)

    # 读取文件一行内容
    while True :
        mline = mfile.readline()
        if "" == mline :
            break
        print(mline)
    mfile.close()

    # 读取文件多行内容
    mlines = mfile.readlines()
    print(mlines)