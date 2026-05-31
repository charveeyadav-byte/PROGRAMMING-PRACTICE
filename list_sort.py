numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Original List:", numbers)

numbers.sort()

print("Sorted List (Ascending):", numbers)

numbers.sort(reverse=True)

print("Sorted List (Descending):", numbers)
