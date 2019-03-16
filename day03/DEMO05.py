def show(date) :
    y = int(date[0:4])
    m = int(date[4:6])
    d = int(date[6:])
    print(y,m,d)
    if y%100!=0 and y%4==0 or y%100==0 and y%400==0 :
        print("闰年")
        a = 0
        num = 0
        while a<m :
            if (a==1)or(a==3)or(a==5)or(a==6)or(a==8)or(a==10) :
                num += 31
            elif (a==4)or(a==7)or(a==9)or(a==11) :
                num += 30
            elif (a == 2):
                num += 29
            a+=1
        num = num + d
        print("这是{0}年的第{1}天".format(y,num))
    else :
        print(":平年")
        a = 0
        num = 0
        while a < m:
            if (a == 1) or (a == 3) or (a == 5) or (a == 6) or (a == 8) or (a == 10):
                num += 31
            elif (a == 4) or (a == 7) or (a == 9) or (a == 11):
                num += 30
            elif (a == 2):
                num += 28
            a += 1
        num = num + d
        print("这是{0}年的第{1}天".format(y, num))

if __name__ == '__main__':
    show("20120902")
