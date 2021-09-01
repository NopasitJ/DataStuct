print("*** Rabbit & Turtle ***")
d, Vr, Vt ,Vf = input("Enter Input : ").split()
D= int(d)
R= int(Vr)
T= int(Vt)
F= int(Vf)

if D<=5000 and R<= 5000 and T<= 5000 and F <=5000 and F>T and F>R:
    s = float(F*(D/(T-R)))
    print("%.2f" %(s))
