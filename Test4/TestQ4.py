def shell_sort(inp, count):
    kk = 4
    while kk > 0:
        for i in range(kk, len(inp)):
            temp = inp[i]
            j = i
            count +=1
            while j >=kk and inp[j-kk] > temp:
                count += 1
                inp[j] = inp[j-kk]
                j-=kk
            inp[j] = temp
        kk //=2
    return count

count = 0

print(" *** Shell sort ***")
inp = [int(k) for k in input("Enter some numbers : ").split(" ")]
r = shell_sort(inp, count)
print()
print(inp)
print("Data comparison = ",r)
