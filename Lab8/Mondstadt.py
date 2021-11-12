def checking(l,x,y):
    k = l[x] if x*2 > len(l)-2 else  l[x] + l[x*2] + l[x*2+1]  
    a = l[y] if y*2 > len(l)-2 else  l[y] + l[y*2] + l[y*2+1]
    if k>a:
        return str(x) + '>' +str(y) 
    elif k<a:
        return str(x) + '<' +str(y)
    else:
        return str(x) + '=' +str(y)

inp = input("Enter Input : ").split('/')
l = [int(e) for e in inp[0].split()]
kk = [e for e in inp[1].split(',')]
print(sum(l))
for i in kk:
    i = i.split()
    print(checking(l, int(i[0]),int(i[1])))