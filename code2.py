def solution(a, b):
    answer = 0
    for index, ai in enumerate(a):
        answer += ai * b[index]
    return answer