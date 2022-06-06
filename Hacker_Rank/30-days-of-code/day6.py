test_case_num = int(input().strip())

i = 0
s = []

while(i < test_case_num):
    input_str = input().strip()
    s.append(input_str)
    i += 1

for item in s:
    # even
    for i, c in enumerate(item):
        if i % 2 == 0:
            print(c, end='')
    print(' ', end='')
    # odd
    for i, c in enumerate(item):
        if i % 2 != 0:
            print(c, end='')
    print(' ')