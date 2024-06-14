from primePy import primes

def largest_prime_factor(num):
    highest = 1
    for i in range(num/2):
        if (num % i == 0) & primes.check(i):
            highest = i

    return i
print(largest_prime_factor(600851475143))