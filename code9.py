#출처 : https://school.programmers.co.kr/learn/courses/30/lessons/181913
#문자열 여러번 뒤집기
def solution(my_string, queries):
   my_string = list(my_string)
   for q in queries:
        a,b = q
        #문자열 뒤집기 진행하기
        my_string = my_string[:a] + list(reversed(my_string[a:b +1])) + my_string[b+1:]
   return ''.join(my_string)