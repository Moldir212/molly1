#КОММЕНТЫ ДЛЯ СЕБЯ
#1
# Импортируем класс datetime (это для работы с датой)
# и timedelta (а это получается у нас для изменения даты)
from datetime import datetime, timedelta
# тут мы получаем текущую дату и время
now = datetime.now()
# так вычитаем 5 дней из текущей даты
newd = now - timedelta(days=5)
#и выводим новую дату
print(newd)

#ввод: 2024-06-01 12:00:00
#вывод: 2024-05-27 12:00:00

#2
from datetime import datetime, timedelta
# Получаем текущую дату
today = datetime.now()
# Вчера = сегодня минус 1 день
yesterday = today - timedelta(days=1)
# Завтра = сегодня плюс 1 день
tomorrow = today + timedelta(days=1)
# Выводим результаты
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#ввод: 2024-06-01 12:00:00
#вывод:
#Yesterday: 2024-05-31 12:00:00
#Today: 2024-06-01 12:00:00
#Tomorrow: 2024-06-02 12:00:00

#3
from datetime import datetime
# Получаем текущее время
now = datetime.now()
# Заменяем микросекунды на 0
without_microseconds = now.replace(microsecond=0)
# Выводим результат
print(without_microseconds)

#ввод: 2024-06-01 12:00:00.123456
#вывод: 2024-06-01 12:00:00


#4
from datetime import datetime
# Создаем первую дату
date1 = datetime(2008, 4, 10, 17, 0, 0)
# Создаем вторую дату
date2 = datetime(2026, 2, 22, 13, 46, 0)
# Находим разницу
difference = date2 - date1
# Выводим разницу в секундах
print("Difference in seconds:", difference.total_seconds())

#ввод: 2008-04-10 17:00:00 и 2026-02-22 13:46:00
#вывод: Difference in seconds: 567648360.0
