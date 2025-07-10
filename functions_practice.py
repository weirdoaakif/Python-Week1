def greet(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")


def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b



def is_even(num):
    """Checks if a number is even."""
    if num % 2 == 0:
        return True
    else:
        return False
    
def factorial(n):
    """Returns the factorial of a number."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def maximum(a, b):
    """Returns the maximum of two numbers."""
    if a > b:
        return a
    else:
        return b
    
# TEST CALLS
greet("Aakif")
print("Sum:", add_numbers(5, 7))
print("Is 4 even?", is_even(4))
print("Factorial of 5:", factorial(5))
print("Max of 8 and 12:", maximum(8, 12))
   