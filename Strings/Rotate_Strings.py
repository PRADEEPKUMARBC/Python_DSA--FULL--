s = "abcde"
goal = "cdeab"

def RotateString(s):
    if len(s) != len(goal):
        return False
    
    cur_s = s
    n = len(cur_s)
    for i in range(0, n):
        if cur_s == goal:
            return True
        cur_s = cur_s[-1] + cur_s[:-1]
    return False
print(RotateString(s))

def RotateString(s):
    if len(s) != len(goal):
            return False
    double_s = s + s
    if goal in double_s:
        return True
    return False
print(RotateString(s))