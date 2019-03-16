if __name__ == '__main__':
    mdict = {"name":"zhnagsan","age":"18"}
    print(type(mdict))

    # 这种遍历字典的方式取出的数据是字典中的每一个键
    for k in mdict :
        # 输出k的类型，类型为str
        print("k is {0}".format(type(k)))

        # 这种遍历字典的方式取出的数据是字典中的每一个值
    for k in mdict.values():
        # 输出k的类型，类型为str
        print("k.values is {0}".format(type(k)))
        print(k)


