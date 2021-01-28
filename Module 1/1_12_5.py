"""
	Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в
	три строки сначала максимальное, потом минимальное, после чего оставшееся число.
	На ввод могут подаваться и повторяющиеся числа.
"""

a = int(input())
b = int(input())
c = int(input())

sumNumbers = a + b + c

if (a >= b) and (a >= c):
	maxNumber = a
elif (b >= a) and (b >= c):
	maxNumber = b
else:
	maxNumber = c

if (a <= b) and (a <= c):
	minNumber = a
elif (b <= a) and (b <= c):
	minNumber = b
else:
	minNumber = c

print(maxNumber)
print(minNumber)
print(sumNumbers - maxNumber - minNumber)
