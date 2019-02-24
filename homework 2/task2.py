

b = input()  # (less - better)
a = input()  # (more - better)
x = 0
lst_a = []
lst_b = []
list_b = []
list_a = []
num_of_nulls = 0
if int(a) < 0:
    a = ''.join(sorted(a, reverse=True))
    a = a[:-1]
    a = ("-" + a)

elif int(a) == 0:
    a = 0
else:
    a = ''.join(sorted(a))
    for zz in range(len(a)):
        list_a.append(a[zz])
    if a.count('0'):
        for i in range(len(a)):
            if a[i] == "0":
                num_of_nulls += 1
            else:
                break
        list_a[0] = list_a[num_of_nulls]
        list_a[num_of_nulls] = 0
        a = ''.join(str(list_a))
        a = a.replace("[", "")
        a = a.replace(" ", "")
        a = a.replace(",", "")
        a = a.replace("'", "")
        a = a.replace("]", "")
if int(b) < 0:
    b = ''.join(sorted(b))
    if b.count('0'):
        for z in range(len(b)):
            list_b.append(b[z])
            if b[z] == "0":
                continue
            if b[z] == "-":
                continue
            lst_b.append(b[z])
        min_not_null = lst_b[0]
        min_not_null_index = b.find(min_not_null)
        list_b[1] = min_not_null
        list_b[min_not_null_index] = 0
        b = ''.join(str(list_b))
        b = b.replace("[", "")
        b = b.replace(" ", "")
        b = b.replace(",", "")
        b = b.replace("'", "")
        b = b.replace("]", "")

elif int(b) == 0:
    b = 0
else:
    b = ''.join(sorted(b, reverse=True))
print(int(b) - int(a))
