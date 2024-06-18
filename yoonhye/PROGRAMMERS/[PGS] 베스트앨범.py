# 속한 노래가 많이 재생된 "장르"를 먼저 수록
# 장르 내에서 많이 재생된 "노래"를 먼저 수록
# 장르 내에서 재생 횟수가 같은 노래 중 고유 번호가 낮은 노래를 먼저 수록
# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 return

from collections import defaultdict

def solution(genres, plays):
    answer = []
    info = defaultdict(list)
    genre_info = defaultdict(int)
    i = 0
    for genre, play in zip(genres, plays):
        info[genre].append((play, i))
        genre_info[genre] += play
        i += 1

    sorted_lst = list(zip(genre_info.values(), genre_info.keys()))
    sorted_lst.sort(reverse=True)

    for value, key in sorted_lst:
        lst = info[key]
        lst.sort(key=lambda x: (-x[0], x[1]))
        answer.append(lst[0][1])
        if (len(lst) >= 2):
            answer.append(lst[1][1])

    return answer