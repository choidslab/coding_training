#!/bin/python3

import math
import os
import random
import re
import sys

# Function Reference: https://minnit-develop.tistory.com/17
def get_binary_num(n, lists):
    a, b = divmod(n, 2)
    lists.append(b)
    if a == 0:
        return lists
    else:
        return get_binary_num(a, lists)

    answerList = []
    answer = get_binary_num(n, answerList)

    return "".join([str(_) for _ in answer])


def find_max_one(lists):
    # Count Consecutive One
    one_cnt = 0
    # Max Count of Consecutive One
    max_cnt = 0

    # Count Consecutive One
    for one in lists:
        if one == 1:
            one_cnt += 1
        else:
            # if element were 0, compare one_cnt and max_cnt
            if one_cnt > max_cnt:
                max_cnt = one_cnt
            # assign 0 to one_cnt variable for the recount
            one_cnt = 0

    # Before return max_cnt variable, compare one_cnt to max_cnt
    if one_cnt > max_cnt:
        max_cnt = one_cnt

    return max_cnt


if __name__ == '__main__':
    n = int(input().strip())
    binary_list = []
    binary_list = get_binary_num(n, binary_list)
    binary_list.reverse()

    print(find_max_one(binary_list))
