if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max_data = max(arr)

    remove_data = {max_data}

    new_list = [i for i in arr if i not in remove_data]

    print(max(new_list))

