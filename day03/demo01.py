def a ():
    pass

if __name__ == '__main__':
    nlist = list()
    for i in range(1,10) :
        nlist.append(i**2)
    print(nlist)

    mlist = [i**2 for i in range(1,10)]
    print(mlist)

     
