
#출처 : https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 롤케이크 자르기
#테스트 통과 2개, 시간초과 문제 발생
def solution(topping):
    answer = 0
    for idx in range(1, len(topping)):
        if len(set(topping[:idx])) == len(set(topping[idx:])):
            answer += 1
    return answer