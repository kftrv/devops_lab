

N = int(input())
lst = []
for a in range(0, N):
    cmmnd = input().split()
    if cmmnd[0] == "insert":
        lst.insert(int(cmmnd[1]), int(cmmnd[2]))
    elif cmmnd[0] == "print":
        print(lst)
    elif cmmnd[0] == "remove":
        lst.remove(int(cmmnd[1]))
    elif cmmnd[0] == "append":
        lst.append(int(cmmnd[1]))
    elif cmmnd[0] == "sort":
        lst.sort()
    elif cmmnd[0] == "pop":
        lst.pop()
    elif cmmnd[0] == "reverse":
        lst.reverse()
    else:
        print("ERROR")
