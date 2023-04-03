import random
length=int(input("Enter the length for the password :"))
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="0123456789"
d="*?!.,:;"
all=a+b+c+d
password="".join(random.sample(all,length))
print("Your can use this as password :",password)
