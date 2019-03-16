if __name__ == '__main__':

    arr = [1,2,3,4,5,6,7,8,9]
    #使用for in
    for i in arr :
        for j in arr[0:i]:
            print(i, end="*"), print(j, end="="), print(i * j, end=" ")
            if j==i:
                print()

    # 使用while
    i=1
    while i<=9 :
         j = 1
         while j<=i :
             print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
             if i == j :
                 print()
                 break
             j += 1
         i += 1