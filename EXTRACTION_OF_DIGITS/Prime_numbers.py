def prime_numbers(n):
    num = n
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

print(prime_numbers(5))

# Better Soultion

def check_prime(n):
    num = n
    result = {}
    for i in range(1, num + 1):
        if num % i == 0:
            result[i] = True
    return result

print(check_prime(100))

# Optimal Solutions
