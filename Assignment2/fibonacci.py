def fibRegular(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


def fibRecursive(n):
    if n <= 1:
        return n
    return fibRecursive(n - 1) + fibRecursive(n - 2)

n = int(input("Enter value of n: "))
print("Fibonacci sequence using regular function:")
fibRegular(n)

print("\nFibonacci sequence using recursive function:")

for i in range(n):
    print(fibRecursive(i), end=' ')
