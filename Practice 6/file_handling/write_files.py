from pathlib import Path

# Создаем файл и записываем данные
file_path = Path("sample.txt")

with open(file_path, "w") as file:
    file.write("Hello, this is the first line\n")
    file.write("This is the second line\n")

print("File created and written successfully!")

# Добавляем новые строки
with open(file_path, "a") as file:
    file.write("This line is appended\n")

print("New data appended!")


#1
with open("output.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
print("File created: output.txt")

#2
with open("output.txt", "a") as f:
    f.write("Third line (appended)\n")
    f.write("Fourth line (appended)\n")
with open("output.txt", "r") as f:
    print(f.read())

#3
try:
    with open("new_file.txt", "x") as f:
        f.write("Created with mode x\n")
    print("new_file.txt created!")
except FileExistsError:
    print("File already exists!")

#4
students = ["Alice\n", "Bob\n", "Charlie\n", "Diana\n", "Eve\n"]
with open("students.txt", "w") as f:
    f.writelines(students)
with open("students.txt", "r") as f:
    print(f.read())

#5
data = [
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 92),
]
with open("grades.txt", "w") as f:
    f.write("Name,Grade\n")
    for name, grade in data:
        f.write(f"{name},{grade}\n")
with open("grades.txt", "r") as f:
    print(f.read())