# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 내적
def solution(a, b):
    answer = 0
    for index, ai in enumerate(a):
        answer += ai * b[index]
    return answer