try:
   val = 10 / 0
   num=int(input("Enter a number:"))
   print(num)

except Exception as err:
    print(err)
except ValueError:
    print("value enter is wrong")
