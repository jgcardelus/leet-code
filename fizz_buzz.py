
def fizz_buzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return "FizzBuzz"
    if n % 5 == 0:
        return "Fizz"
    if n % 3 == 0:
        return "Buzz"
    return n

for i in range(1, 16):
    print(fizz_buzz(i))
