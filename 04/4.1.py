lst = [0, 1, 0, 3, 12, 11, 0, 5]
a = 0

for null in lst:
    if null != 0:
        lst[a] = null
        a +=1

for i in range(a, len(lst)):
    lst[i] = 0


print(lst)