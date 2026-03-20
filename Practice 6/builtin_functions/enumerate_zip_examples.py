names = ["Ali", "Aruzhan", "Dias"]
scores = [85, 90, 78]

# enumerate()
for index, name in enumerate(names):
    print(index, name)

# zip()
for name, score in zip(names, scores):
    print(name, score)

# sorted()
nums = [5, 2, 9, 1]
print("Sorted:", sorted(nums))

# type conversion
x = "123"
y = int(x)
print(type(y), y)




#1
fruits = ["apple", "banana", "cherry", "date"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

#2
names = ["Alice", "Bob", "Charlie"]
scores = [92, 85, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

#3
data = [34, 12, 56, 7, 89, 23]
print(f"Original : {data}")
print(f"Sorted   : {sorted(data)}")
print(f"Length   : {len(data)}")
print(f"Sum      : {sum(data)}")
print(f"Min      : {min(data)}")
print(f"Max      : {max(data)}")

#4
print(int("42"), type(int("42")))
print(float("3.14"), type(float("3.14")))
print(str(100), type(str(100)))
print(bool(0), bool(1), bool(""))
print(list((1, 2, 3)), tuple([4, 5, 6]))

#5
keys = ["name", "age", "city"]
values = ["Alice", 25, "Almaty"]
profile = dict(zip(keys, values))
print(profile)
for i, (k, v) in enumerate(profile.items()):
    print(f"[{i}] '{k}' → {v} (type: {type(v).__name__})")