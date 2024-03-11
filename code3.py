from collections import Counter
def solution(friends, gifts):
    answer = 0
    gift_dict = {}
    for friend in friends:
        gift_dict[friend] = {'send': 0, 'received': 0, 'result': 0}

    for gift in gifts:
        a, b = gift.split(' ')
        gift_dict[a]['send'] += 1
        gift_dict[b]['received'] += 1
    
    
    for val in gift_dict:
        gift_dict[val]['index'] =  gift_dict[val]['send'] - gift_dict[val]['received']
    
    for f in friends:
        receiver = [g.split(' ')[1] for g in gifts if g.split(' ')[0] == f]
        not_receiver = [fr for fr in friends if fr not in receiver and fr != f]
        
        sender = [g.split(' ')[0] for g in gifts if g.split(' ')[1] == f]
        not_sender = [fr for fr in friends if fr not in sender and fr != f]
        c_receiver = Counter(receiver)
        c_sender = Counter(sender)
        
        not_person = [fr for fr in friends if fr not in receiver and fr not in sender and fr != f]
        for i in not_receiver:
            c_receiver[i] = 0
        for i in not_sender:
            c_sender[i] = 0

        if len(not_person) != 0:
            for person in not_person:
                if gift_dict[person]['index'] < gift_dict[f]['index']:
                    gift_dict[f]['result'] += 1
        for c in c_receiver.items():
            for s in c_sender.items():
                if c[0] == s[0]:
                    if c[1] > s[1]:
                        gift_dict[f]['result'] += 1
                    if c[1] == s[1] and c[1] != 0:
                        if gift_dict[f]['index'] > gift_dict[c[0]]['index']:
                            gift_dict[f]['result'] += 1
                    
    answer = [gift['result'] for gift in gift_dict.values()]    
    return max(answer)