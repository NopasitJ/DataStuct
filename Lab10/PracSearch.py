def bs(left,right,l,k):
    if left > right:
        return "Not found"
    mid = (right + left)//2
    if l[mid] == k:
        return "Found"
    return bs(mid+1,right,l,k) if l[mid] < k else bs(left,mid-1,l,k)

inp = input("Enter Input : ").split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bs(0, len(arr) - 1, sorted(arr), k))