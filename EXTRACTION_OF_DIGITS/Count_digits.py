def count_digits(n):
    num = n
    count = 0
    while num > 0:
        count += 1
        num = num // 10
        return count

count = count_digits(5873)
print(count)