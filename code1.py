# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/250121
# [PCCE 기출문제] 10번 / 데이터 분석

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    standard = ['code', 'date','maximum','remain']
    
    val_index = standard.index(ext)
    sort_index = standard.index(sort_by)
    answer = [d for d in data if d[val_index]  < val_ext]
    
    return sorted(answer, key=lambda data: data[sort_index])