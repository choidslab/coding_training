num1 = int(input().strip())
num2 = int(input().strip())

first_pos = int(num2 / 100)
second_pos = int((num2 % 100) / 10)
third_pos = num2 % 10

first_line = num1 * third_pos
second_line = num1 * second_pos
third_line = num1 * first_pos

print(first_line)
print(second_line)
print(third_line)
print(first_line + second_line * 10 + third_line * 100)
