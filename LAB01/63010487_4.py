def odd_list(ls):
    eqr =[]
    for i in range(0,len(ls)):
        if(ls[i]==1):
            eqr.append(ls[i])
        elif(ls[i]%2 == 1):
            eqr.append(ls[i])
    return eqr
   
print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
