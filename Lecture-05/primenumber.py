def generate_primes(n):
    primes = []


    for num in range(2, n + 1):
        print(num,n)
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            print(num)
            print(i)
            if num % i == 0:
                is_prime = False
                break

        print("______________")
        print(num)
        if is_prime:
            primes.append(num)
            print("HERE")
    return primes

print(generate_primes(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]