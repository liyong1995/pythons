if __name__ == '__main__':
    #两种创建列表的方式
    mlist = list([1,2,3,4]) #等效于 mlist=[1,2,3,4]
    print(type(mlist))
    print(mlist)




    mlist  = list([1,2,3])
    mlist1 = [1,2,3]
    print(type(mlist))
    print(type(mlist1))
    # 在末尾追加元素
    mlist.append(4)
    print(mlist)
    # 在指定坐标位置追加元素
    mlist.insert(6,20)
    print(mlist)
    # 返回指定元素的索引
    a = mlist.index(20)
    print(a)
    # 使用pop删除元素，无参时默认最后一位，有参时是按照索引删除
    a = mlist.pop()
    print(a)
    # 使用del删除元素，可以直接删除列表对象，并且不能输出
    del mlist[0]
    print(mlist)
    # 使用remove按照指定元素删除
    mlist.remove(2)
    print(mlist)

    # 一次性清空所有元素
    mlist.clear()
    print(mlist)