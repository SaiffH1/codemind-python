N = int(input())  # Read the value of N from the user

for _ in range(N):
    a, b = map(int, input().split())  # Read two integers from each line and assign them to variables a and b
    sum = a + b  # Calculate the sum of the two numbers
    print(sum)  # Print the sum on a separate line
