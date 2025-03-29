#Q 1: Separate even & Odd numbers in a list
def separate_even_odd(numbers: list) -> tuple: #: list → This is a type hint indicating that numbers should be a list and -> tuple tells that the function returns a tuple
    even_numbers = [num for num in numbers if num % 2 == 0] #List with even numbers
    odd_numbers = [num for num in numbers if num % 2 != 0]  # List with even numbers
    return  even_numbers, odd_numbers  # Returning as a tuple



#Q 2: Find prime number in a list
def is_prime(n: int) -> bool:
    #Condition to check if a number is a Prime.
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i:
            return False
    return True

def find_primes(numbers: list) -> tuple:
    prime_numbers = tuple(num for num in numbers if is_prime(num))
    return prime_numbers  # Returning as a tuple




sample_list = [10, 501, 22, 37, 100, 999, 87, 351]

print(f"Given list of numbers: {sample_list}")
#Q 1: output
even,odd = separate_even_odd(sample_list)
print("\nQ1: Separate even & Odd numbers in a list: ")
print(f"Even Number: {even},\nOdd Numbers: {odd}")

#Q 2: output
primes = find_primes(sample_list)
print("\nQ2: Find prime number in a list: ")
print(f"Prime Numbers: {primes}")