# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


print("Введите  число.")
n = int(input())


list = []

x = n * -1

while x <= n:
    list.append(x)
    x += 1



print(list)


numbers = [1, 5, 3]
data = open('file.txt', 'w')
data.write(str(numbers[0]))
data.write(' \n')
data.write(str(numbers[1]))
data.write(' \n')
data.write(str(numbers[2]))
data.close()

result = 1
path = 'file.txt'
data = open(path, 'r')

for line in data:
    result *= list[int(line)]

print(result)

