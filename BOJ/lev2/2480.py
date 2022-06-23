num1, num2, num3 = map(int, input().split())

if num1 == num2 == num3:
    print(10000 + num1 * 1000)

elif num1 == num2:
    print(1000 + num1 * 100)

elif num2 == num3:
    print(1000 + num2 * 100)

elif num3 == num1:
    print(1000 + num3 * 100)

else:
    num_list = []
    num_list.append(num1)
    num_list.append(num2)
    num_list.append(num3)
    max_num = max(num_list)
    print(max_num * 100)