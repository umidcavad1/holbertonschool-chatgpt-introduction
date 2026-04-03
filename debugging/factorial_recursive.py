#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Error: negative number"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    print(factorial(num))
except ValueError:
    print("Error: please enter a valid integer")
