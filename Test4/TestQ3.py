def bubble(l):
    for i in range(len(l)-1):
        for j in range(0,len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

print(" *** Bubble sort ***")
ss = input("Enter some numbers : ")
s1 = [int(e) for e in ss.split()]
s2 = [int(e) for e in ss.split()]
s2 = bubble(s1.copy())

count = 0
for i in range(len(s1)):
    if s1[i]==s2[i]:
        count+=3
if s1==s2:
    count+=1
print()     
print(s2)
print("Data comparison =",   str(int(len(s1)*((len(s1)-1)/2)-count)))