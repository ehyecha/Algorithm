

def check_word(w, words):
    answer = 0
    for wo in words:
        if w.startswith(wo):
            answer += 1
            w = w[len(wo):]
            break
    return answer, w, wo

def include(w, words):
    isInclude = False
    for wo in words:
        if w.startswith(wo):
            isInclude = True
            break
    return isInclude

def check(word):
   go = True
   words = ["aya","ye", "woo", "ma"]
   results = 0
   while go: 
       result, word, wo = check_word(word, words)
       index = words.index(wo)
       del words[index]
       results += result
       if word == '':
           go = False
       elif not include(word, words):
           go = False
           results = 0
   return results


def solution(babbling):
    answer = []    
    for index in range(0, len(babbling)):
        answer.append(check(babbling[index]))
    return len([a for a in answer if a != 0])