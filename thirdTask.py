# Створіть програму, яка перевіряє текст на неприпустимі слова

import re


readedString = ""
excludedWord = ""
numEntries = 0

with open("thirdText.txt", "r") as myFile:  # читаємо текст з файлу та зберігаємо його в рядок
    readedString = myFile.read()
# далі будемо працювати з вмістом файла, як з рядком
while True:  # цикл для запиту від користувача та первинної обробки слова, яке ввів користувач
    excludedWord = input("Введіть заборонене слово: ")
    if len(excludedWord) == 0:  # якщо користувач не ввів нічого
        print("Веедіть слово, що складається щонайменше з 1 букви!")
        continue
    elif re.fullmatch(r'\b\w+\b', excludedWord) is None:  # перевірка, за допомогою регулярного виразу
                                                                 # чи є словом, а не набором спецсимволів
                                                                 # введений рядок
        print("Введений рядок не є словом")
        continue
    break

numEntries = readedString.count(excludedWord)  # порахуємо кількість входжень забороненого слова

if numEntries == 0:  # якщо заборонене слово не знайдено в тексті, повідомимо про це та завершимо виконання програми
    print("Введене заборонене слово не знайдено! Вхідний текст не змінено!")
elif numEntries > 0:  # якщо заборонене слово знайдено, виконаємо заміну цього слова на "зірочки"
    readyString = readedString.replace(excludedWord, "*" * len(excludedWord))
    with open("thirdText.txt", "w") as myFile:
        myFile.write(readyString)
    print(f"Статистика: Виконано {numEntries} замін(и) забороненого слова {excludedWord}")
