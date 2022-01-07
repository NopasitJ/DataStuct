i = int(input("Input : "))
if i>0:
    for kk in range(i):
        print(kk*'*'+(i*2-kk*2)*' '+kk*'*')
    for kk in range(i,0,-1):
        print(kk*'*'+(i*2-kk*2)*' '+kk*'*')
else:
    print("!!!Please enter number greater than zero!!!")