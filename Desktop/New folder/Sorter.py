import random

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

lower = min(a, b)
upper = max(a, b)

answer = input("Will you let me generate random numbers? (y/n): ").strip().lower()

if answer == 'y':
    array = [random.randint(lower, upper) for i in range(100)]
    for item in array:
        print(item)
else:
    print("Cancelled")
