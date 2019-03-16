import random

def ra (num):
    mlist = [random.randint(1,num) for i in range(1,11) ]

    for i in range(num) :
        num1 = random.randrange()
        mlist.append(num1)
    print(mlist)

    n = random.randint(0,num)

    for i in mlist :
        if n == i :
            print("在")
        else:
            print("不在")




if __name__ == '__main__':


    num = int(input("请输入一个整数："))
    ra(num)
