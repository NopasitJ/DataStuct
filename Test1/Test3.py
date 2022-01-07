i = [int(x) for x in input("Enter number end with (-1) : ").split()]
data = [0]*(max(i)+1)
j=[]
found =0
if -1 not in i:
    print("Invalid INPUT !!!")
else:
    for x in i:
        if x !=-1:
            data[x]+=1
            j.append(x)
        else:
            break
    for y in j:
        if data[y] > len(j)/2:
            print(y)
            found =1
            break
    if found == 0:
        print("Not found")
