

Nnm = input()
nm = []
ip = []
o_tmp = []
gg = 0
j = 0
for i in range(int(Nnm)):
    nm.append(input())
Nip = input()
while j < (int(Nip)):
    ipt = (input())
    ip = ipt.split(" ")
    gc = 0
    for k in range(int(Nnm)):
        mask_k = nm[k].split(".")
        for kip in range(2):
            ip_k = ip[kip].split(".")
            for ip_oct in range(4):
                o_tmp.append(int(mask_k[ip_oct]) & int(ip_k[ip_oct]))
        if o_tmp[0:4] == o_tmp[4:8]:
            gc += 1
        o_tmp.clear()
        gg = gg + gc
        gc = 0
    j += 1
    print(gg)
    gg = 0
