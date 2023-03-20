is_male=False
if_female=True
is_tall=True

if is_male and is_tall:
    print("you are male")
elif not(if_female):
    print("you are female")
else:
    print("you identify as others")


print("enter the number:")
n=24

if (n % 2) != 0:
    print("Weird")
elif ( n % 2 == 0) and 2<=n<=5:
    print("Not Weird")
elif (n % 2 == 0) and 6<=n<=20:
    print("Weird")
else :
    print("Not Weird")




def max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num1 < num2 and num2 > num3:
       return num2
    else:
        return num3

print(max(13,5,10))

a=6
b=3

print(a // b)
print(a / b )
