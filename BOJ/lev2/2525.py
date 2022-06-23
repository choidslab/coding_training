hour, min = map(int, input('').split())
timer = int(input())

if min + timer >= 60:
    carry_hour = (min + timer) // 60
    hour += carry_hour
    min = (min + timer) % 60

    if hour >= 24:
        hour = hour - 24
else:
    min = min + timer

print(hour, min)
