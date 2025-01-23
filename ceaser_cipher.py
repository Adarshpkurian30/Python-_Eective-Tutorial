


message = input("Enter your message: ")
shift = int(input("Enter the shift (code): "))
print("Choose an option:")
print("1. Encrypt")
print("2. Decrypt")
choice = int(input("Enter your choice (1 or 2): "))
result = ""
# Function to shift characters
def shift_char(char, shift_amount, is_encrypt=True):
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        offset = (ord(char) - start + (shift_amount if is_encrypt else -shift_amount)) % 26
        return chr(start + offset)
    return char
if choice == 1:
    for char in message:
        result += shift_char(char, shift)
    print("Encrypted Message:", result)
elif choice == 2:
    for char in message:
        result += shift_char(char, shift, is_encrypt=False)
    print("Decrypted Message:", result)
else:
    print("Invalid choice!")
