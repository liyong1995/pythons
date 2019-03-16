if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 使用for in
    for i in arr:
        for j in arr[0:i]:
            a = i*j
            print(i, end="*"), print(j, end="="), print(str(a).rjust(2), end=" ")
            if j == i:
                print()

    j=0
    for i in range(120) :
       j += 1


       print(str(i).rjust(3),end=" ")

       if (j % 10 == 0):
           print()

