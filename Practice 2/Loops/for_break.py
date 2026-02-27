#Ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":#if the code find the value "banana", the loop will stop and exit, and it will not print the remaining values in the list.
    break
  
#Ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)