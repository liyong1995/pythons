class Myexc(Exception) :
    # 自己定义的异常类
    def show(self):
        print("hehe")

if __name__ == '__main__':
    # 创建一个对象
    me = Myexc()

    # 调用对象方法
    me.show()

    try :
        raise Myexc
    except Myexc as e:
        print("Myexc")

        # 调用了自定义异常的扩展了 的方法
        print(e)
