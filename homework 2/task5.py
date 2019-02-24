import operator


a = input()
full_lst = []
dct = {}
for i in range(len(a)):
    full_lst.append(a[i])
orig_lst = sorted(set(full_lst))
for i in orig_lst:
    dct[i] = full_lst.count(i)
for i in range(3):
    mx = max(sorted(dct.items()), key=operator.itemgetter(1))[0]
    print(mx, dct[mx])
    del dct[mx]
