print(" *** Wind classification ***")
S = float(input("Enter wind speed (km/h) : "))
if S>0 and S<51.99:
    print("Wind classification is Breeze.")
elif S>52.00 and S<55.99 :
    print("Wind classification is Depression.")
elif S >56.00 and S<101.99 :
    print("Wind classification is Tropical Storm.")
elif S>102.00 and S<208.99 :
    print("Wind classification is Typhoon.")
elif S>= 209.00:
    print("Wind classification is Super Typhoon.")