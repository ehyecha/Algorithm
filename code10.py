#출처: https://school.programmers.co.kr/learn/courses/30/lessons/181943
#문제: 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    my_string = my_string[:s] + overwrite_string + my_string[s+ len(overwrite_string):]
    return my_string