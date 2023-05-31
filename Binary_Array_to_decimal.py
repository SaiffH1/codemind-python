def binary_to_decimal(binary_array):
    decimal_value = 0
    power = len(binary_array) - 1

    for bit in binary_array:
        decimal_value += bit * (2 ** power)
        power -= 1

    return decimal_value
n = int(input())
binary_array = list(map(int,input().split())) 
decimal_value = binary_to_decimal(binary_array)
print(decimal_value)
