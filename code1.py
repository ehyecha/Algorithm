
def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    standard = ['code', 'date','maximum','remain']
    
    val_index = standard.index(ext)
    sort_index = standard.index(sort_by)
    answer = [d for d in data if d[val_index]  < val_ext]
    
    return sorted(answer, key=lambda data: data[sort_index])