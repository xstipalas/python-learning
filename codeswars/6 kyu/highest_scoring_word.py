score = {chr(i): i - 96 for i in range(ord('a'), ord('z') + 1)}

def high(x):
    def word_score(word):
        return sum(score[l] for l in word)
    
    words = x.split()
    return max(words, key=word_score)
