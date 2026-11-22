# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143


def prime_factor(n):
    p_factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            p_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        p_factors.append(n)
    print(p_factors)
    print(p_factors[-1])

prime_factor(600851475143)
