if __name__ == '__main__':
    username = input("请输入用户名：")
    password = input("请输入密码：")

    if len(username) >=6 and len(username) <=16 :
        if '*' not in username or '#' not in username  or '!' not in username:

            if len(password) >= 6 and len(password) <= 16:
                if '*' not in password or '#' not in password or '!' not in password:
                    print("符合要求")
                else:
                    print("密码出现了*#")
            else:
                print("密码不符合要求")
        else :
            print("用户名出现了*#")
    else :
        print("用户名不符合要求")


