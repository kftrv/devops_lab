

N = input()
oldest_id = -1
mx = 0
for i in range(int(N)):
    in_str = input()
    a1 = int(in_str.split(' ')[0])
    s1 = int(in_str.split(' ')[1])
    if int(a1) > mx and int(s1) == 1:
        mx = a1
        oldest_id = i + 1
print(oldest_id)
