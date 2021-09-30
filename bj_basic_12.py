#1

n = int(input())


numbers = []


for _ in range(n):
    numbers.append(int(input()))

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

for n in numbers:
    print(n)


#2

from sys import stdin

n = int(stdin.readline())

arr = []

for i in range(n):
    arr.append(int(stdin.readline())

arr.sort()

for i in arr:
    print(i)
