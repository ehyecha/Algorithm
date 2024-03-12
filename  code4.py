def solution(bandage, health, attacks):
    successive_score = 0

    current_health = health
    idx = 0
    for time in range(0, attacks[-1][0] + 1):
        attack_time = [i[0] for i in attacks]
        attack_degree = [i[1] for i in attacks]
        
        if time in attack_time:
            current_health -= attack_degree[idx]
            idx += 1
            successive_score = 0
        else:
            temp_health =  current_health + bandage[1]
            if current_health < health and temp_health <= health:
                current_health += bandage[1]
        
        if successive_score == bandage[0]:
             current_health +=bandage[2]
        successive_score += 1
        if current_health  <= 0:
            return -1
    
    return  current_health