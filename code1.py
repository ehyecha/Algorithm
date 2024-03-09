

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    standard = ['code', 'date','maximum','remain']
    val_index = standard.index(ext)
    sort_index = standard.index(sort_by)
    answer = [d for d in data if d[val_index]  < val_ext]
    
    sorted(answer, key=lambda data: data[sort_index])
    
    return answer


result = solution(data, 'code',3,'remain')
print(result)