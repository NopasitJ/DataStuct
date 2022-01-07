import math
class MyInt:
    def __init__(self,number):
        self.number = number
    def isPrime(self):
        if self.number<2 :
            return str(self.number) + ' isPrime : False'
        for i in range(2,int(math.sqrt(self.number)+1)):
            if self.number%i==0:
                return str(self.number) + ' isPrime : False'
        return str(self.number) + ' isPrime : True' 
    def showPrime(self):
        print('Prime number between 2 and ' + str(self.number) +' : ',end='')
        if self.number<=1:
            return '!!!A prime number is a natural number greater than 1'
        k = self.number
        kk =[]
        w =[0]*(k+1)
        for i in range(2,k+1):
            if w[i]==0:
                kk.append(i)
                for j in range(i,k+1,+i):
                    w[j]=1
        return ' '.join([str(i) for i in kk])
    def __sub__(x,y):
        return str(x.number) + ' - ' + str(y.number) + ' = ' + str(x.number - int(y.number/2))
print(' *** class MyInt ***')
num = [int(e) for e in input('Enter 2 number : ').split()]
x = MyInt(num[0])
y = MyInt(num[1])

print(x.isPrime())
print(y.isPrime())
print(x.showPrime())
print(y.showPrime())
print(x-y)