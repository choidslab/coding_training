alarm = 45
hour, min = map(int, input('').split())

# min 값이 음수가 되는 경우 60분을 더해준다.
if min - alarm < 0:
    hour -= 1
    min = (min - 45) + 60
    # hour 값이 음수가 되면 24시간 표기법이므로 24를 더해준다.
    if hour < 0:
        hour = hour + 24
else:
    min -= 45

print(hour, min)