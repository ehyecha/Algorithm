#출처: https://school.programmers.co.kr/learn/courses/30/lessons/92341
#문제: 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT >주차 요금 계산


def solution(fees, records):
    answer = []
    record = {}
    
    for r in records:
        a,b,c = r.split(' ')
        if not b in record:
            record[b] = [c,a]
        else:
            record[b].append([c,a])
    print(record)

    return answer