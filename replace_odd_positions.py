num = input("Enter a number: ")

digit_count = len(num)
print("Number of digits:", digit_count)

result = ""

for i in range(len(num)):
    if (i + 1) % 2 != 0:  # Odd position
        result += "0"
    else:
        result += num[i]

print("Modified number:", result)
