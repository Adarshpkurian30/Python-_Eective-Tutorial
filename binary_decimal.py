binary = input("Enter the binary number: ")
decimal = 0
power = 0

for digit in binary[::-1]:
    if digit not in "01":
        print("Invalid input: Not a binary number.")
        exit()
    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal:", decimal)
