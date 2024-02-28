#!/usr/bin/env python3

def print_fibonacci(length):
    # initialize fibonacci_sequence with first two no.s
    fibonacci_sequence = [0,1]
    
    for n in range(length -2):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(fibonacci_sequence[:length])

print_fibonacci(9)