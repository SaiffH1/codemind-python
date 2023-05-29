def is_disarium(number):
    # Convert the number to a string
    number_str = str(number)
    length = len(number_str)
    total = 0

    # Iterate through each digit and calculate the sum
    for i, digit in enumerate(number_str):
        total += int(digit) ** (i + 1)

    # Check if the total is equal to the number
    return total == number

# Example usage:
num = int(input())
if is_disarium(num):
    print("True")
else:
    print("False")
