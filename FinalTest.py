def new(a):
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return b

li = [1,2,3,4,5,6,7,8,9]
print(new(li))