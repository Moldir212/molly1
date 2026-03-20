import os

# Создание папок
os.makedirs("test_dir/sub_dir", exist_ok=True)
print("Directories created!")

# Текущая директория
print("Current directory:", os.getcwd())

# Список файлов
print("Files and folders:", os.listdir())

# Удаление папки
# os.rmdir("test_dir/sub_dir")  # только если пустая



import os

#1
print(f"Current directory: {os.getcwd()}")
os.makedirs("project_demo", exist_ok=True)
print("Created: project_demo/")

#2
os.makedirs("project_demo/src/utils", exist_ok=True)
os.makedirs("project_demo/tests", exist_ok=True)
print("Created nested: project_demo/src/utils/ and project_demo/tests/")

#3
for name in ["a.py", "b.txt", "c.csv"]:
    with open(f"project_demo/{name}", "w") as f:
        f.write("")

items = os.listdir("project_demo")
print(f"Contents of project_demo/: {items}")

#4
for item in os.listdir("project_demo"):
    if item.endswith(".py"):
        print(f"Python file: {item}")

#5
original = os.getcwd()
os.chdir("project_demo")
print(f"Changed to: {os.getcwd()}")
os.chdir(original)
print(f"Back to: {os.getcwd()}")

import shutil
shutil.rmtree("project_demo")
print("Cleaned up project_demo/")