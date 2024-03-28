#출처 : https://www.acmicpc.net/submit/31561/75781890
#문제 : 백준 2024 상반기 전남대학교 PIMM 알고리즘 파티 > 시계탑

def solution():
    n = int(input())
    return  15 + (n -30) * 1.5 if  n >= 30 else n/2
