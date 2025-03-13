def has_duplicates(f):
    e = {}
    for x in f:
        if x in e:
            return True
        e[x] = True
    return False
def has_duplicates2(f):
   
    return len(set(f)) < len(f)
if __name__ == '__main__':
    f = [1, 2, 3]
    print has_duplicates(f)
    f.append(1)
    print has_duplicates(f)
    f = [1, 2, 3]
    print has_duplicates2(f)
    f.append(1)
    print has_duplicates2(f)