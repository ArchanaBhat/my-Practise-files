def longest_word(array):
    result=[]
    for i in array:
        result.append((len(i),i))
    result.sort()
    return result[-1][1]

print(longest_word(["archana","teju","subash","max"]))
