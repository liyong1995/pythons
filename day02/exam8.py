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

    nlist = [str(i).strip() for i in klist]
    nset = set()
    for i in nlist:
        nset.add(str(i).strip())
    ndict = {}
    for i in nset:
        num = nlist.count(i)
        ndict[i] = nlist.count(i)
    print(type(ndict))
    print(ndict)











