# Check Wheather the number is Armstrong or not

def check_armstrong(n):
    num = n
    total = 0
    nod = len(str(n))
    while num > 0:
        ld = num % 10
        total = total + ( ld ** nod)
        num = num // 10
    return n == total

armstrong = check_armstrong(153)
if armstrong:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")