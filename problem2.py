def problem2(limit):
    fibonacci_list = []
    fibonacci_list.append(1)
    fibonacci_list.append(2)
    lower = 1
    upper = 2
    newnum = lower + upper
    while(newnum < limit):
        fibonacci_list.append(newnum)
        lower = upper
        upper = newnum
        newnum = lower + upper

    sum_evens = 0
    for num in fibonacci_list:
        if(num % 2 == 0):
            sum_evens += num
    return sum_evens

print(problem2(4000000))