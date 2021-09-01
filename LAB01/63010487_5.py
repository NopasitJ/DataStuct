a = int(input("Enter Input : "))
for x in range (0,2*a+4):
    for y in range (0,2*a+4):
        if x+y<a+1:
            print(".",end="") ###จุดชุดซ้าย
        elif x+y < 2*a+3 and x< a+2 and y<a+2 :
            print("#",end="") ###ช้าปจากบรรทัดแรกลงฐาน
        elif x==0 or x==a+1 :
            print("+",end="")### +แนวนอนยาว
        elif x>0 and x<a+1 and (y==a+2 or y==2*a+3):
            print("+",end="") ###+ครอบช้าปบน
        elif x>0 and x<a+2 and (y>a+2 or y<2*a+3):
            print("#",end="") ### #ในกรอบ+
        elif x>a+1 and y<a+2 and (x==a+2 or x==2*a+3):
            print("#",end="") ### #ตอนกลับ
        elif x>a+1 and y<a+2 and (y==0 or y==a+1):
            print("#",end="") ### #สร้างกรอบ
        elif x>a+1 and y<a+2 and (y>0 or y<a+1):
            print("+",end="")### +ในกรอบ
        elif x>a+1 and y>a+1 and x+y<3*a+6:
            print("+",end="")### +ตอนกลับแทน#
        else:
            print(".",end="")### . ปิดท้าย
    print()
