def hbd(age):
    x=(age//2)
    y=(age%2)
    if y==0 :
     i =20
    else : i =21
    J="saimai is just " + '%d'%(i) + ", in base "+ '%d'%(x) +"!"
    return J

year = input("Enter year : ")

print(hbd(int(year)))