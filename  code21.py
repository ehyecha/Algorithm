#출처: https://school.programmers.co.kr/learn/courses/30/lessons/135808
#문제 : 코딩테스트 연습 > 연습문제 >과일 장수

#k는 사과한상자의 최저점, m 한상자에 들어가는 사과 개수, 
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    for i in range(0,len(score),m):
        if len(score[i: i+m]) == m:
            answer += min(score[i: i+m]) * m * 1
    return answer