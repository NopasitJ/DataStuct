def reverse(lst):
    if not lst: 
        return lst
    return lst[-1:] + reverse(lst[:-1])
x =  list(map(int,input('Enter your List : ').split(',')))
x.sort()
print("List after Sorted : ",reverse(x),sep="")