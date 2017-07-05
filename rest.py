def palindrome():
    entered_num=input("enter the no.")
    num = entered_num
    rev=0
    while num>0:
        var=num%10
        rev=rev*10+var
        num=num/10
    return entered_num, rev
a,b= palindrome()
if (a==b):
    print a,"is a palindrome no."
else:
    print a,"is not a palindrone no."

