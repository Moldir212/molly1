# json.py

import json  # подключаем модуль для работы с JSON

# Создаем обычный Python-словарь
person = {
    "name": "Moldir",
    "age": 18,
    "city": "Almaty"
}

#Преобразование Python → JSON строка

# json.dumps() превращает словарь в JSON-строку
json_data = json.dumps(person)

print("JSON string:", json_data)
# Результат будет примерно:
# {"name": "Moldir", "age": 18, "city": "Almaty"}


#Преобразование JSON → обратно в Python

# json.loads() превращает JSON-строку обратно в словарь
parsed_data = json.loads(json_data)

# Доступ к значению по ключу
print("Name:", parsed_data["name"])


#Запись JSON в файл

# Открываем файл в режиме записи ("w")
with open("person.json", "w") as file:
    
    # json.dump() записывает словарь в файл в формате JSON
    json.dump(person, file)
#Чтение JSON из файла
# Открываем файл в режиме чтения ("r")
with open("person.json", "r") as file:
    
    # json.load() читает JSON из файла и превращает в словарь
    data = json.load(file)

print("Read from file:", data)
# Результат будет примерно:
# Read from file: {'name': 'Moldir', 'age': 18, 'city': 'Almaty'}
