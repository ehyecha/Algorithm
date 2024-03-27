#출처 : https://www.acmicpc.net/submit/31561/75781890
#문제 : 백준 > 시계탑

n = int(input())
answer = 0
if n >= 30:
    n -= 30
    answer = 15 + n *(3/2)
else:
    answer= n / 2
print(answer)