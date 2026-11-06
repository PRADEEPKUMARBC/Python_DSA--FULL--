s = "ahsdfhsadbskfdhkij"
q = ["d", "a", "y", "u"]

hash_list = [0] * 26

for char in s:
    ascii_value = ord(char)
    index = ascii_value - ord('a')
    hash_list[index] += 1

print(hash_list)

for ch in q:
    ascii_value = ord(ch)
    index = ascii_value - 97
    print(hash_list[index])