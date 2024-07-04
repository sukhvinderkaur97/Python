mylist = ["apple", "banana", "cherry", "grapes", "papaya"]

print(len(mylist))

print(mylist[2:4])

if "apple" in mylist:
  print("Yes, 'apple' is in the fruits list")
  
mylist[1] = "berry"
print(mylist)

mylist[1:3] = ["blackcurrant", "watermelon"]
print(mylist)

mylist.append("orange")
print(mylist)

mylist.insert(1, "papaya")
print(mylist)

tropical = ["mango", "pineapple", "papaya"]
mylist.extend(tropical)
print(mylist)

mylist.remove("blackcurrant")
print(mylist)

mylist.pop()
print(mylist)

del mylist[4]
print(mylist)

mylist.sort()
print(mylist)

mylist.clear()
print(mylist)

