def match_words(words):
    case = 0
    list = []
    for word in words:
        if len (word) > 1 and word [0] == word [-1]:
            case += 1
            list.append(word)
    print("list of words with first and last charrcter",list)
    return case 
a = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print (a)