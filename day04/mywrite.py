if __name__ == '__main__':
    mfile = open(r"a.c","w")

    num = mfile.write("gundan")
    with open(r"a.c","r") as mfile :
        mlist = list(mfile)
        print(mlist)






