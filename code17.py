#출처: https://school.programmers.co.kr/learn/courses/30/lessons/131704 
#문제: 코딩테스트 연습 >연습문제 >택배상자


def solution(order):
    answer, sub = initcontainer(order)
    for i in order[answer:]:
        if i == sub[-1]:
            answer += 1
            sub.pop()
        else:
            break
    return answer       

def initcontainer(order):
    container = [ i +1 for i in range(len(order))]
    sub_container = []
    result = 0

    for o in order:
        if len(sub_container) > 0 and o == sub_container[-1]:
            result += 1
            sub_container.pop()
            break;
        for j in container:
            if o == j :
                result += 1
                break
            else:
                sub_container.append(j)
    return result, sub_container

print(solution([4,2,1,3]))