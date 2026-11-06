def func(sum, i, N):
    if i > N:
        print(sum)
        return
    sum = sum + i
    func(sum , i+1, N)


    

func(0, 1, 10)