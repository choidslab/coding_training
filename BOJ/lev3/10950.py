test_case = int(input())

results_of_sum = []

for _ in range(test_case):
    num1, num2 = map(int, input().split())
    results_of_sum.append(num1 + num2)

for result in results_of_sum:
    print(result)
