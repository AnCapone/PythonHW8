# Створіть програму, яка перевіряє текст на неприпустимі слова

import re


readedString = ""
excludedWord = ""
numEntries = 0

with open("thirdText.txt", "r") as myFile:
    readedString = myFile.read()

while True:
    excludedWord = input("Введіть заборонене слово: ")
    if len(excludedWord) == 0:
        print("Веедіть слово, що складається щонайменше з 1 букви!")
        continue
    elif re.fullmatch(r'\b\w+\b', excludedWord) is None:
        print("Введений рядок не є словом")
        continue

numEntries = readedString.count(excludedWord)

if numEntries == 0:
    print("Введене заборонене слово не знайдено! Вхідний текст не змінено!")
else:
    readyString = readedString.replace(excludedWord, "*" * len(excludedWord))
    with open("thirdText.txt", "w") as myFile:
        myFile.write(readyString)
