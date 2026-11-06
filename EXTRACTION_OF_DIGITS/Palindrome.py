
def check_palindrome(n):
    num = n
    result = 0
    while num > 0:
        Ld = num % 10
        result = (result * 10) + Ld
        num = num // 10
    return n == result

check = check_palindrome(12321)
if check:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")