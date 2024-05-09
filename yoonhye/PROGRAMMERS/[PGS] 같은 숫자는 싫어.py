#연속적으로 나타나는 숫자 제거하고 반환
def solution(arr):
    answer = [arr[0]]
    for v in arr[1:]:
        if answer[-1] != v:
            answer.append(v)

    return answer