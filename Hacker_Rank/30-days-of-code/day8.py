# 여러 줄에 걸쳐 정수 입력 받는 방법
# n = int(input())
# nums = [int(input()) for _ in range(n)]
# print(nums)

### My Solution1 ###
iter = int(input().strip())
i = 0
phone_book = {}

# Key, Value 입력
while i < iter:
    key, value = input('').split()
    phone_book.update({key: int(value)})
    i += 1
# for i in range(0, iter):
#     key, value = input().split()
#     phone_book[key] = value

# 이 부분에서 Runtime Error 발생 -> Test Case 1 (100,000)에서 에러
# Input이 많아지면 List는 성능에 굉장한 영향을 미친다.
# 불필요하므로 제거하고 아래의 for 문에서 검색할 Key를 입력 받도록 수정
search_key = [input() for _ in range(iter)]

# 검색 결과 출력
for key in search_key:
    if key in phone_book.keys():
        print(f'{key}={phone_book[key]}')
    else:
        print('Not found')

### My Solution2 ###
iter = int(input().strip())
i = 0
phone_book = {}

# Key, Value 입력
while i < iter:
    key, value = input('').split()
    phone_book.update({key: int(value)})
    i += 1

for i in range(0, iter):
    try:
        # 검색할 Key 입력
        key = input()
        # key가 있는지 검사
        if key in phone_book:
            # key가 있다면 key=value 출력
            print(f"{key}={phone_book[key]}")
        else:
            # key가 없으면 Not found 출력
            print("Not found")
    except:
        break


# Stack Overflow Solution
# n, Enter number of record you need to insert in dict
n = int(input())
d = dict()

# enter name and number by separate space
for i in range(0, n):
    name, number = input().split()
    d[name] = number
# print(d)      #print dict, if needed

# enter name in order to get phone number
for i in range(0, n):
    try:
        name = input()
        if name in d:
            print(f"{name}={d[name]}")
        else:
            print("Not found")
    except:
        break