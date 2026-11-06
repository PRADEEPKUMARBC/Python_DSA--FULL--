m = [10,111,2,3,4,5,6,7,8,9]
n = [2,1,3,5,7,1,9,3,10]

for num1 in m:
    count = 0
    for num2 in n:
        if num1 == num2:
            count += 1
    print(num1,num2,count)