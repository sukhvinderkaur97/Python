mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(mytuple[1])

y = list(mytuple)
y.append("orange")
mytuple = tuple(y)
print(y)

x = list(mytuple)
x.remove("apple")
mytuple = tuple(x)
print(x)