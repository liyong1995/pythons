if __name__ == '__main__':
    mset = {1,2,3,3,4,4,5}
    nset = {7,9,8,3,4}
    gset = nset^mset
    nset.union(mset)
    print(gset)