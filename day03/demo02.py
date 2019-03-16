if __name__ == '__main__':
    mlist = [1,2,3]
    nlist = ["a","b","c"]

    qlist = []
    for m in mlist :
        for n in nlist :
            qlist.append(str(m)+n)
    print(qlist)



    plist = [str(m)+n for m in mlist for n in nlist]
    print(plist)

    plist = [str(m)+n
             for m in mlist \
                if m%2!=0 \
             for n in nlist]
    print(plist)




    





