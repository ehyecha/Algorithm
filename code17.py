#출처: https://school.programmers.co.kr/learn/courses/30/lessons/131704 
#문제: 코딩테스트 연습 >연습문제 >택배상자


def solution(order):
    answer, sub = initcontainer(order)
    print('answer sub', answer, sub)
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
        print('sub ', result, sub_container, o)
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

def solution(order):    
    stack = []    
    answer = 0
    for idx,num in enumerate(order):
        stack.append(idx +1)
        while stack and stack[-1] == order[answer]:                   
            stack.pop()
            answer += 1                         
    return answer


print(solution([5,4,3,2,1]))