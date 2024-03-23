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