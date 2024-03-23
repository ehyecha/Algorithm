#출처: https://school.programmers.co.kr/learn/courses/30/lessons/138476
#문제: 코딩테스트 연습> 연습문제 > 귤 고르기

from collections import Counter
def solution(k, tangerine):
    cte = Counter(tangerine)
    keys = []
    for i in cte.most_common():
        k = k - i[1]
        keys.append(i[0])
        if k <= 0:
            break
    return len(keys)