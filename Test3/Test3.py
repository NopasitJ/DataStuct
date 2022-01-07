def  isPalindrome(a):
    if   len (a)<=1:
        return True
    return  a[0] == a[len (a)- 1] and isPalindrome(a[1:len (a)-1])

kk = input('Enter Input : ')
l = ""
for i in kk:
    if i.isalpha():
        l += i.lower()
ans = "'" + kk + "'"
if   isPalindrome(l):
    print (ans,"is palindrome")
else :
    print (ans,"is not palindrome")