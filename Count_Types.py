import string

def count_types(text):
    upper = 0
    lower = 0
    num = 0
    punct = 0
    space = 0
    for i in text:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            num += 1
        elif i in string.punctuation:
            punct += 1
        else:
            space += 1
    myList = [("upper", upper), ("lower", lower), ("punctuation", punct), ("space", space), ("numeral", num)]

    myDict = dict(myList)
    for i, j in list(myDict.items()):
        if j == 0:
            del myDict[i]
    return myDict


a = "aaa asd A!2"
print(count_types(a))