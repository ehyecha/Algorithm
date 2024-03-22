#출처: https://school.programmers.co.kr/learn/courses/30/lessons/140107
#문제: 코딩테스트연습 > 연습문제 > 점찍기
import math

def solution(k, d):
    answer = 0
    ak = [ i for i in range(0, 1+d, k)]
    for a in ak:
        y = int(math.sqrt(d**2 - a**2))
        answer += y // k +1
    return answer