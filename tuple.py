mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(mytuple[1])

y = list(mytuple)
y.append("orange")
mytuple = tuple(y)
print(y)