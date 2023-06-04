def cheecking(word):
    i=0
    while i != (len(word)-i-1):
        if word[i] != word[-i-1]:
            return False
        else:
            i=i+1
    return True
print(cheecking('kajak'))