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
    vlist = [
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

    keylist = [str(i).strip() for i in klist]
    valuelist = [str(i).strip() for i in vlist]
    kset = set(keylist)
    vset = set(valuelist)

    kklist = list(kset)
    vvlist = list(vset)
    print(kset)
    print(vset)

    ndict = {}

    for i in kklist :

        ndict[i] = vvlist[kklist.index(i)]
    print(ndict)
