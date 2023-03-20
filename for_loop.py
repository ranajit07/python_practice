friends=["josh","mike","tom","haka"]
numbers=(1,2,6,12,53,12)
for num in numbers:
    print(num,end= " ")

for index in range(3,10):

    print(index)

print("index of friend")
for index in range(len(friends)):

    print(friends[index])

n=3
for num in range(n):
   print(num * num)


def is_leap(year):
    leap = False
    # Python program to check if year is a leap year or not


    if (year % 400 == 0) and (year % 100 == 0):
       year=True

    elif (year % 4 == 0) and (year % 400 == 0):
        year=True
    else:
        year=False


    return leap




year = 2000
print(is_leap(year))
x=1
y=1
z=1
n=2
x=x+1
y=y+1
z=z+1
list_2=[]
for i in range(x):
    for j in range(y):
        for k in range(z):
            if i+j+k != n:
                list=[i,j,k]
                list_2.append(list)

print(list_2)



# Driver code
arr = [2,3,6,6,5]
n = 5

mx = max(arr)
sc=None
for num in arr:
    if num==mx:
        pass
    elif sc==None:
        sc=num
    elif num > sc:
        sc=num
print(sc)






