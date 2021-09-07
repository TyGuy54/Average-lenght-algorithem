sentance1 = input("write a sentance: ")

def solution(sentance):
    for p in "!?,:.":
        sentance = sentance.replace(p, ' ')

    words = sentance.split()
    return round(sum(len(word) for word in words)/ len(words), 2)

print(solution(sentance1))