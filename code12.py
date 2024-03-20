def solution(num, total):
    answer = []
    sum = (num -1) * (num) //2
    answer = [n + (total - sum) // num for n in range(num)]
    return answer
