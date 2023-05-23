def is_ugly_number(number):
    if number <= 0:
        return False

    ugly_factors = [2, 3, 5]

    for factor in ugly_factors:
        while number % factor == 0:
            number //= factor

    return number == 1

# Example usage
number = int(input())
if is_ugly_number(number):
    print(f"Ugly Number")
else:
    print(f"Not Ugly Number")
