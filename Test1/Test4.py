x = int(input("Enter a positive number : "))
if x < 0:
    print(x,"is too low.")
elif x>=16:
    print(x,"is too high.")
else:
    print(" ".join(["%X"%(i) for i in range(1,x+1)]))
    for j in range(2,x):
        print("%X"%(j)+(x*2-3)*" " + "%X"%(j-1))
    print("%X "%(x) + ' '.join(["%X"%(i) for i in range(1,x) ]))
