message = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

# 1. Посчитать количество символов
length = len(message)
print("1. Колличество символов: ", length)

# 2. Развернуть строку.
def reverse_string(message):
    return message[::-1]
print("2. Результат переворота строки: ", reverse_string(message))

# 3. Сделать каждое слово с большой буквы
print("3. Каждое слово с большой буквы: ", message.title())

# 4. Сделать весь текст прописными буквами
print("4. Сделать весь текст прописными буквами: ", message.upper())

# 5. Найти число вхождений "нд", "ам", "о" в строку
count_nd = message.count("нд")
count_am = message.count("ам")
count_o = message.count("о")
print("5. Найти число вхождений в строку: ", f"'нд': {count_nd},", f"'ам': {count_am},", f"'о': {count_o}.")

# 6. Собственные упражнения
reverse = ""
for word in message.split():
    reverse = "{} {}".format(reverse, word[::-1])
print("6.1. Результат переворота всех слов в предложении: ", reverse)

swapped_message = message.swapcase()
print("6.2. Изменение регистра букв на противоположный:", swapped_message)

# 7. Развернуть предложение.
words = message.split()  
reversed_words = words[::-1]  
reversed_message = " ".join(reversed_words)  
print("7. Результа переворота предложения: ", reversed_message)

# 8. Вывести в консоль исходную строку
print("8. Исходная строка: ", message)