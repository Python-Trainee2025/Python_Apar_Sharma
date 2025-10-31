number = int(input("Enter a number: "))
is_prime = True
for i in range(2, int(number/2) + 1):
    if number % i == 0:
        print(f"{number} is not a prime number.")
        is_prime = False
        break

if is_prime:
    print(f"{number} is a prime number.")