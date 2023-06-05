def cheecking(word):
    i=0
    if len(word)%2==1:
        while i!=(len(word)-i-1):
            if word[i] != word[-i-1]:
                return False
            else:
                i=i+1
        return True
    else:
        while i!=(len(word)-i):
            print(len(word)-i)
            if word[i] != word[-i-1]:
                return False
            else:
                i=i+1
        return True
print(cheecking('kajak'))