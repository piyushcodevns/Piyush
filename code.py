def find_prime_numbers(n):
    """Return a list of prime numbers up to n."""
    loopcount=0
    primecount=0
    if n < 2:
        return []
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                loopcount+=1
                is_prime = False
                break
        if is_prime:
            primecount+=1
            primes.append(num)
    return primes,loopcount, primecount
    


# def custom_pattern(n):

#     result = [4] * (n // 3)
#     result.append(2)
#     return result


# print(custom_pattern(20))
primes,loopcount, primecount=find_prime_numbers(500)

print("Prime numbers:", primes)
print("Total loop iterations:", loopcount)
print("Total prime numbers found:", primecount)

