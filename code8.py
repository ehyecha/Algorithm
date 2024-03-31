
#출처 : https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 롤케이크 자르기
#테스트 통과 2개, 시간초과 문제 발생
from collections import Counter

def solution(topping):
    answer = 0
    for idx in range(1, len(topping)):
        if len(Counter(topping[:idx])) == len(Counter(topping[idx:])):
            answer += 1
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))


print(Counter([1,2,3,4]) == Counter([1,2,3]))