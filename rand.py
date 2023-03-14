import random
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

numbers = list(range(A,B))
print(numbers)

C = round(random.random(),3)
print(C)

D = random.randint(A, B)
print(D)

E = random.randrange(A, B)
print(E)

for s, value in enumerate(numbers, 1):
    print(s, value)