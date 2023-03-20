friends=["mike","josh","david","jim","jim","hogan"]
number=[1,4,2,6,3,5]

friends.sort()
print(friends)
friends.extend(number)
print(friends)
friends.append("creed")#insert value at end
print(friends)
friends.insert(1,"kelly") #insert value at specified index
print(friends)
print(friends[1] )
print(friends[-1] )#from backword
print(friends[1:])
friends.pop() #remove the last value
print(friends.count("jim"))
print(friends.reverse())
print(friends)
friends.clear()
print(friends)
