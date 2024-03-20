#출처: https://school.programmers.co.kr/learn/courses/30/lessons/120923
#문제: 연속된 수의 합

def solution(num, total):
    answer = []
    sum = (num -1) * (num) //2
    answer = [n + (total - sum) // num for n in range(num)]
    return answer
