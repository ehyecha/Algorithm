#출처: https://school.programmers.co.kr/learn/courses/30/lessons/154539
#문제: 코딩테스트 연습 > 연습문제 >뒤에 있는 큰 수 찾기

#정확성: 82.6

def solution(numbers):
    answer = [-1] * len(numbers)
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[j] > numbers[i]:
                answer[i] = numbers[j]
                break
    return answer

#보완된 솔루션
def solution(numbers):
    stack = []
    answer = [-1] *len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack[-1]] = numbers[i]
            stack.pop()
        stack.append(i)

    return answer
