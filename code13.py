# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/250125
# PCCE 기출문제 [PCCE 기출문제] 9번/ 이웃한 칸

def solution(board, w, h):
    n = len(board)
    count = 0
    dh = [0,1,-1,0]
    dw = [1, 0,0,-1]
    h_check = [0,0,0,0]
    w_check = [0,0,0,0]
    
    for i in range(4):
        w_check[i] = w + dw[i]
        h_check[i] = h + dh[i]
   
    for i in range(4):
        if w_check[i] >= 0 and w_check[i] < n and h_check[i] >= 0 and h_check[i] < n:
            if board[w][h] == board[w_check[i]][h_check[i]]:
                count += 1
    
    return count

