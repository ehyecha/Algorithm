#출처 https://school.programmers.co.kr/learn/courses/30/lessons/60057
#문제 코딩테스트 연습 2020 KAKAO BLIND RECRUITMENT 문자열 압축


def solution(s):
    max_cnt = int(len(s) / 2)
    target = []
    if len(s) ==1:
        return s
    for i in range(1, max_cnt +1):
        answer = ''
        recursive = 0
        pre = ''
        for j in range(0, len(s), i):
            cur = s[j:j+i]
            if (pre != cur):
                recursive = 0
                answer += cur
                pre = cur
            else:
                recursive += 1
                answer = answer[:len(answer) - i]
                if recursive > 1:
                    answer = answer[: -len(str(recursive))]
                answer += "{}{}".format(recursive + 1, cur)
        target.append(len(answer))       
    return min(target)

a = solution("a")
print(a)

# s = 'dsafdsa'
# print(s[-1])