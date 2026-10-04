def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

count = int(input("Enter the number of Fibonacci terms to generate: "))
print(fibonacci_sequence(count))