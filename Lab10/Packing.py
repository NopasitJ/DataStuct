def packing(l, k):
    res = 1
    pack = k
    for i in range(len(l)):
        if pack >= l[i]:
            pack -= l[i]
        else:
            res += 1
            pack = k - l[i]
    return res

inp = input("Enter Input : ").split('/')
l,k = list(map(int,inp[0].split())),int(inp[1])
i_min = max(l)
while packing(l,i_min) != k:
    i_min+=1
print("Minimum weigth for",k,"box(es) =",i_min)