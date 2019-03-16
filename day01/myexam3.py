import random
if __name__ == '__main__':
    num1 = int(input("请输入一个整数："))
    num2 = int(random.randrange(0,99999,2))
    if num1>num2 :
        print(str(num1)+">"+str(num2))
    else:
        print(str(num1)+"<"+str(num2))