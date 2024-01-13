# Даний текстовий файл. Підрахувати кількість слів у ньому

import re

result = []
with open("secondFile.txt", "r") as myFile:
    result = re.findall(r'\b\w+\b',myFile.read())

quantityOfWords = len(result)

print(f"Number of words: {quantityOfWords}")