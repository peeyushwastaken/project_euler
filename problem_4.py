# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99. Find the largest palindrome made from the product of two 3-digit numbers

def palindrome(n):
    lst=[]
    rev=[]
    while n>0:
        lst.append(n%10)
        n//=10
    rev=lst.copy()
    rev.reverse()
    if lst == rev:
        return True
    else:
        return False

final=[]
a=999
i = 999
while a > 100:
    x = a * i
    if palindrome(x) == True:
        final.append(x)
    if i == 100:
        i=999
        a-=1
    i-=1

aloo = max(final)
print("the largest palindrome is ",aloo)