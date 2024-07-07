from collections import defaultdict

def get_cases(n, cases, dice):
    new_cases = defaultdict(list)
    for key, value in cases.items():
        for i in range(int(key) % 10 + 1, n):
            for a in dice[i]:
                for b in value:
                    new_cases[key + str(i)].append(a + b)
    return new_cases

def find_wining_case(n, cases):
    numbers = set(range(0, n))
    max_count = 0
    final_dices = 0
    i = 0
    for key in cases.keys():
        i += 1
        if i > len(cases) // 2:
            break
        rest_dices = numbers - set(map(int, list(key)))
        rest_dices_num = 0
        for num in rest_dices:
            rest_dices_num *= 10
            rest_dices_num += num
        rest_dices_num = str(rest_dices_num)

        win_dice_combination, count = compare(key, rest_dices_num, cases, n)
        if max_count < count:
            final_dices = win_dice_combination
            max_count = count
    return final_dices


def compare(a, b, cases, n):
    count1 = 0
    count2 = 0
    cases[a].sort()
    cases[b].sort()
    len_b = len(cases[b])
    for d1 in cases[a]:
        result, index = binary_search(cases[b], d1)
        if result:
            count2 += len_b - (index + 1)
            while (index >= 0 and cases[b][index] == d1):
                index -= 1
            count1 += index + 1
        else:
            count1 += index
            count2 += (len_b - index)

    if count1 > count2:
        return (a, count1)
    else:
        return (b, count2)

def binary_search(arr, num):
    start = 0
    end = len(arr) - 1

    while (end >= start):
        m = (start + end) // 2
        if arr[m] == num:
            while (m < len(arr) and arr[m] == num):
                m += 1
            return (True, m - 1)
        elif arr[m] > num:
            end = m - 1
        else:
            start = m + 1
    return (False, start)


def solution(dice):
    answer = 0
    n = len(dice)
    cases = defaultdict(list)
    for i in range(n):
        cases[str(i)] = dice[i]

    for i in range(2, n // 2 + 1):
        cases = get_cases(n, cases, dice)

    answer = find_wining_case(n, cases)
    answer = list(map(lambda x: int(x) + 1, answer))

    return answer