# 等边三角形的方法

def dengbian(bian) :
    # bian代表等边三角形的边长
    i=1
    while i<=bian :
        j = i
        while j<=(2*bian-1)//2 :
            print(" ",end="")
            j+=1
        k = 0
        while k<i :
            print("*",end=" ")
            k+=1
        print()
        i+=1


# 九九乘法表的方法

def jiujiu(hang) :
    # hang代表要展示的行数
    i=1
    while i<=hang :
        j = 1
        while j <=i :
            h = str(i*j).rjust(2)
            print(str(j)+"*"+str(i)+"="+h,end="  ")
            if i==j :
                print()
            j+=1
        i+=1


# 菱形方法

def lingxing(num) :
    for i in range(num+1) :
        print(" "*(num-i+1),end="")
        print(" *"*i,sep=" ")
    for j in range(num) :
        print(" "*(j+2),end="")
        print(" *"*(num-j-1),sep=" ")

# 给定一个数字，每10个换行，右对齐

def youduiqi(num) :

    mlist = str(num)[:]
    mlen = len(mlist)
    counts = 0
    for i in range(num):
        counts += 1
        print(str(i).rjust(mlen),end=" ")
        if counts %10 == 0 :
            print()

