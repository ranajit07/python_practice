number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],

]

for row in number_grid:
    for col in row:
        print(col)


def transalte(phrase):
    transaltion=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                transaltion = transaltion + "G"
            else:
                transaltion=transaltion+"g"
        else:
            transaltion=transaltion+letter

    return transaltion

print(transalte(input("enter the name:")))
