def findmin(k,a,m):
    if k[a]<m:
        m=k[a]
    if a>0:
        findmin(k,a-1,m)
    if a==0:
        print("Min :",m)

num =[int(i) for i in input('Enter Input : ').split()]
findmin(num,len(num)-1,1e12)