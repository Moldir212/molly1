#Ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) #if the code find the value "banana", it will skip the rest of the code inside the loop for that iteration, and it will not print "banana". Instead, it will continue to the next iteration of the loop and print "cherry".