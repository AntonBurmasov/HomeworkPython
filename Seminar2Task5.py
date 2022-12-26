# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
# (Не используя библиотеки связанные с рандомом)



import uuid
import datetime

random_time = datetime.datetime.now().microsecond * 100000000000000000000000000000 # Можно уменьшить количество знаков в итоговом числе путем умножения на 10000000.....

tok = uuid.uuid4()
print('{:.0f}'.format(tok.int / random_time))