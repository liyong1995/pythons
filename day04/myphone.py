if __name__ == '__main__':

    with open(r"D:\kaosjiwenjian\python\day04\a.png","rb") as a :
        a1 = a.read()
        print(a1)
    with open(r"b.png","wb") as b :
        b.write(a1)