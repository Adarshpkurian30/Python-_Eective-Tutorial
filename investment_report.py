
initial_amount = float(input("Enter the initial deposit: "))
rate = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the number of years: "))
print(f"{'Year':<6} {'Start Balance':<16} {'Interest':<10} {'End Balance':<16}")

balance = initial_amount
for year in range(1, years + 1):
    start_balance = balance
    interest = balance * (rate / 100)
    balance += interest
    # Display results for the current year
    print(f"{year:<6} {start_balance:<16.2f} {interest:<10.2f} {balance:<16.2f}")
