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
    nset = set()
    for i in klist :
        nset.add(str(i).strip())
    print(nset)
    klen = len(klist)
    nlen = len(nset)
    if klen == nlen :
        print("无重复")
    else :
        print("有重复")
