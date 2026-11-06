word = "The Sky is Blue"

def reverseString(word):
    words = word.split()
    n = len(words) - 1
    r_string = []
    while n >= 0:
        r_string.append(words[n])
        n -= 1
    return " ".join(r_string)
print(reverseString(word))