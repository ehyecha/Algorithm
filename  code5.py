def solution(quiz):
    answer = []
    for q in quiz:
        math = q.split(' = ')
        print(math[0], math[1])
        if eval(math[0]) == int(math[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer