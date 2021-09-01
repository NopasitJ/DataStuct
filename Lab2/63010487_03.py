print("*** Odd Even ***")
def odd_even(arr, s):
    if isinstance(arr,list):
        ans = []
        for x in range(0,len(arr)):
            if(s == 'Even' and x%2==1):
                ans.append(arr[x])
            elif(s == 'Odd'and x%2==0):
                ans.append(arr[x])  
    elif isinstance(arr,str):
        ans = ''
        for x in range(0,len(arr)):
            if(s == 'Even' and x%2==1):
                ans+=arr[x]
            elif(s == 'Odd'and x%2==0):
                ans+=arr[x]
    return ans
        

t,s,q = input("Enter Input : ").split(",")
if t == 'S':
    s = str(s)
if t == 'L':
    s = s.split(' ')
print(odd_even(s,q))