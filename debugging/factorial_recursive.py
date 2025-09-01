#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    # Check if argument is provided
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <number>")
        print("Example: python factorial.py 5")
        sys.exit(1)
    
    try:
        # Convert argument to integer
        n = int(sys.argv[1])
        
        # Calculate factorial
        result = factorial(n)
        print(f"Factorial of {n} is: {result}")
        
    except ValueError as e:
        if "invalid literal" in str(e):
            print(f"Error: '{sys.argv[1]}' is not a valid integer")
        else:
            print(f"Error: {e}")
        sys.exit(1)
    except RecursionError:
        print(f"Error: Number too large (recursion limit exceeded)")
        sys.exit(1)

if __name__ == "__main__":
    main()
