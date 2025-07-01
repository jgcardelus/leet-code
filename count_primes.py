class Solution:
    def countPrimes(self, n):
        def is_prime_walking(target, last_prime):
            is_prime = True
            for j in range(last_prime + 1, target):
                if target % j == 0:
                    is_prime = False
                    break

            return is_prime

        counter = 0
        primes = [] # O(n)

        for i in range(2, n-1): # O(n)
            is_prime = True

            for prime in primes:  # O(n)
                if i % prime == 0:
                    is_prime = False
                    break

            if is_prime and len(primes) > 0:
                is_prime = is_prime_walking(i, primes[-1])

            if is_prime:
                primes.append(i)
                counter += 1

        return counter

solver = Solution()
print(solver.countPrimes(10))
print(solver.countPrimes(3))
