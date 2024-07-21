# 처음에 카드 n/3장을 뽑아 모두 가짐
# 각 라운드가 시작할 때 카드를 두 장 뽑음
# 카드 뭉치에 남은 카드가 없다면 게임을 종료
# 카드 한 장당 동전 하나를 소모해서 가질 수 있음
# 카드에 적힌 수의 합이 n+1이 되도록 카드 2장을 내고 다음 라운드로 진행할 수 있음.

from collections import deque


def solution(coin, cards):
    answer = 1
    n = len(cards)
    queue = deque(cards[n//3:])
    picked_card = set(cards[:n//3])
    discard_card = set()
    couple = set()

    for c in picked_card:
        if (n + 1 - c) in picked_card:
            if ((c, n + 1 - c) and (n + 1 - c, c)) not in couple:
                couple.add((c, n + 1 - c))

    while (queue):
        for _ in range(2):
            card = queue.popleft()
            if coin:
                if (n + 1 - card) in picked_card:
                    coin -= 1
                    couple.add((card, n + 1 - card))
                else:
                    discard_card.add(card)

        if len(couple):
            answer += 1
            couple.pop()

        else:
            for c in discard_card:
                if (n + 1 - c) in discard_card:
                    if ((c, n + 1 - c) and (n + 1 - c, c)) not in couple:
                        couple.add((c, n + 1 - c))
                        break
            if len(couple) and coin >= 2:
                c1, c2 = couple.pop()
                discard_card.discard(c1)
                discard_card.discard(c2)
                coin -= 2
                answer += 1
            else:
                break

    return answer