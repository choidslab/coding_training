def factorial(n):
    # Write your code here
    if n <= 1:
        return 1
    else:
        return factorial(n-1) * n


if __name__ == "__main__":
    num = int(input())
    result = factorial(num)
    print(result)
