# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.
import re

result = []
with open("loremIpsum.txt", "r") as myFile:
    result = re.findall(r'\b\w{7,}\b',myFile.read())

with open("minSevenLetters.txt", "w") as myNewFile:
    myNewFile.write(" ".join(result))