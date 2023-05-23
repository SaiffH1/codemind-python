number = int(input())
count = 0 
while number > 0:
    digit = number % 10
    if digit > count:
        count = digit
    number //= 10

print(count)