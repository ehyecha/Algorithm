def isMaxHeal(current, max):
    if current > max:
        current = max
    return current

def solution(bandage, health, attacks):
    successive_score = 0

    current_health = health
    idx = 0
    for time in range(0, attacks[-1][0] + 1):
        successive_score += 1
        attack_time = [i[0] for i in attacks]
        attack_degree = [i[1] for i in attacks]
        
        if time in attack_time:
            current_health -= attack_degree[idx]
            idx += 1
            successive_score = 0
        else:
            if current_health < health:
                current_health += bandage[1]
        
        if successive_score == bandage[0]:
             current_health += bandage[2]
             current_health = isMaxHeal(current_health, health)
                
        if current_health  <= 0:
            current_health = -1
            break;
    
    return  current_health