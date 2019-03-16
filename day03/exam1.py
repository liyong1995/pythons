def show(birth1,birth2) :
    b1 = birth1[0:4]
    b2 = birth1[4:6]
    b3 = birth1[6:]
    b4 = birth2[0:4]
    b5 = birth2[4:6]
    b6 = birth2[6:]
    if b1 > b4 :
        print("{0}年龄大".format(birth1))
    elif b1 < b4 :
        print("{0}年龄大".format(birth2))
    elif b1 == b4 :
        if b2 >b5:
            print("{0}年龄大".format(birth1))
        elif b2 < b5:
            print("{0}年龄大".format(birth2))
        elif b2 == b5:
            if b3 > b6:
                print("{0}年龄大".format(birth1))
            elif b3 < b6:
                print("{0}年龄大".format(birth2))
            elif b3 == b6:
                print("年龄一样大")



if __name__ == '__main__':
    birth1 = input("请输入第一个生日：")
    birth2 = input("请输入第二个生日：")

    show(birth1,birth2)


