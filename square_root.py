

input_number = int(input("Enter a positive number: "))
if input_number <= 0:
    print("Error: Invalid input. Please enter a positive number.")
    exit(1)
current_estimate = input_number
while True:
    next_estimate = 0.5 * (current_estimate + input_number / current_estimate)
    
    if abs(next_estimate - current_estimate) < 0.0001:
        break
    current_estimate = next_estimate
print(f"The square root of {input_number} is approximately: {next_estimate:.4f}")
