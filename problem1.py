def problem1(limit):
    sum = 0
    for i in range(limit):
        if(i % 3 == 0):
            sum += i
        elif(i % 5 == 0):
            sum += i
    return sum

print(problem1(1000))