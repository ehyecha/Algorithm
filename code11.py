#출처: https://school.programmers.co.kr/learn/courses/30/lessons/120924
#문제: 코딩테스트 연습 > 코딩테스트 입문 > 다음에 올 숫자


def solution(common):
    answer = 0
    #등차인지 등비인지 구별
    diff1 =common[1] - common[0]
    diff2 = common[2] - common[1]
    if (diff1 == diff2):
        answer = common[len(common) -1] + diff1
    else :
        answer =  common[len(common) -1] * (diff2 / diff1)
    return answer