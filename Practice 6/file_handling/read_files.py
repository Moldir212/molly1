# Чтение файла разными способами

with open("sample.txt", "r") as file:
    print("Read():")
    print(file.read())

with open("sample.txt", "r") as file:
    print("\nReadline():")
    print(file.readline())

with open("sample.txt", "r") as file:
    print("\nReadlines():")
    lines = file.readlines()
    print(lines)