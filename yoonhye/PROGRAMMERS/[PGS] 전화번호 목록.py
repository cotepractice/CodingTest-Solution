def solution(phone_book):
    info = dict.fromkeys(phone_book, 0)

    for num in phone_book:
        for i in range(1, len(num) + 1):
            if info.get(num[:i]) != None:
                info[num[:i]] += 1
                if info[num[:i]] == 2:
                    return False

    return True