# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/181949
# 대소문자 바꿔서 출력하기

str = input()
str = [s for s in str]
conv_str = [ s.lower() if s.isupper() else s.upper() for s in str]
print(''.join(conv_str))