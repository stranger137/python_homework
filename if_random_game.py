import random

print("Добрый день! Сыграем в игру? Загадайте число от 1 до 4.")
a=int(input())
r = random.randinе(1,4)
if a!=r:
    if a<r:
        print("Ваше число меньше загаданного.")
    else:
        print("Ваше число больше загаданного.")
    print("Повторите еще раз!")
else:
    print("Победа!")