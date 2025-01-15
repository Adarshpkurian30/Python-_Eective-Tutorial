income = float(input("Enter your annual income: "))

total_tax = 0.0

if income <= 300000:
    total_tax = 0.0
elif income <= 700000:
    total_tax = (income - 300000) * 0.05
elif income <= 1000000:
    total_tax = 20000 + (income - 700000) * 0.10
elif income <= 1200000:
    total_tax = 50000 + (income - 1000000) * 0.15
elif income <= 1500000:
    total_tax = 80000 + (income - 1200000) * 0.20
else:
    total_tax = 140000 + (income - 1500000) * 0.30

print(f"Your calculated tax is: ₹{total_tax:.2f}")
