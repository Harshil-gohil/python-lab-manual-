a=int(input("Enter a 4 digit number ="))

i=0
while a>0:
    b= a%10
    i= i+b
    a= a//10

print(i)    


