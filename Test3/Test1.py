def natural_sum(x,k):
    if x>1:
        natural_sum(x-1,k)
    k.append(x)
    return k
print(' *** Natural sum ***')
num = int(input('Enter number : '))
    
print( ' + '.join([str(e) for e in natural_sum(num,[])]),'=',sum(natural_sum(num,[])))