if __name__ == '__main__':
    #文件读
    try :
        mfile = open(r"a.c")
    except :
        print("Exception")
    else :
        mfile.close()
