#Q 1: Separate even & Odd numbers in a list
from itertools import combinations


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
        if n % i==0:
            return False
    return True

def find_primes(numbers: list) -> tuple:
    prime_numbers = tuple(num for num in numbers if is_prime(num))
    return prime_numbers  # Returning as a tuple

# 4. Sum of First and Last Digit of an Integer
def sum_first_and_last_digit(n: int) -> int:
    digit = [int(d) for d in str(n)]
    return digit[0] + digit[-1] #Sun of first and last digit from a given number

# 5. Find Ways to Make Rs. 10 Using Given Coins
def find_a_way_to_make_10(coins):
    # coins = [1,2,5,10]
    ways = []
    for i in range(1,11):
        for combo in combinations(coins,i):
            if sum(combo) == 10:
                ways.append(combo)
    return ways #return a list of tuples
"""
This code also for by using for looping concept
def find_ways_to_make_10():
    coins = [1, 2, 5, 10]  # Available coins
    target = 10  # We want to make Rs. 10

    # Dictionary to store the number of ways to make each amount
    ways_dict = {}

    # List to store all combinations of coins as tuples
    ways_list = []

    # Try all possible combinations of coins (using nested loops)
    for i in range(target // coins[0] + 1):  # Number of 1's we can use
        for j in range(target // coins[1] + 1):  # Number of 2's we can use
            for k in range(target // coins[2] + 1):  # Number of 5's we can use
                for l in range(target // coins[3] + 1):  # Number of 10's we can use
                    # Calculate the total sum for the current combination
                    coin_sum = i * coins[0] + j * coins[1] + k * coins[2] + l * coins[3]

                    # If the sum is Rs. 10, store the combination in the list and dictionary
                    if coin_sum == target:
                        coin_combination = (i, j, k, l)  # A tuple with counts of each coin
                        ways_list.append(coin_combination)  # Store in the list
                        ways_dict[coin_combination] = ways_dict.get(coin_combination, 0) + 1  # Store in the dictionary

    return ways_list, ways_dict
"""

# 6. Find Duplicates in Three Lists
def find_duplicates(list1: list, list2: list, list3: list) -> set:
    return set(list1) & set(list2) & set(list3)  # Set intersection for duplicates


# 7. Find the First Non-Repeating Element in a List
def first_non_repeating(numbers: list) -> int:
    count_dictonary  = {num: numbers.count(num) for num in numbers}
    print(f"Printing how many times the given number {numbers} appears in the list : {count_dictonary}")
    for num in numbers:
        if count_dictonary[num] == 1:
            return num
    return -1

# 8. Find the Minimum Element in a Sorted List
def find_minimum(sorted_list : list) -> int:
    if not sorted_list: # check for the empty list
        return None

    min_element = sorted_list[0]  # Initialize the first element as the minimum

    for num in sorted_list:
        print(f"Checking element: {num}")
        if num < min_element:
            print(f"New minimum found. Previous minimum: {min_element}. Current minimum: {num}")
            min_element = num  # Update min_element if a smaller number is found
            print(f" Now the Minimum Element in a Sorted List : {min_element}")
        else:
            print(f"{num} is not smaller than the current minimum: {min_element}")

    return min_element


# 9. Find a Triplet Whose Sum Equals a Given Value
def find_triplet_with_sum(numbers: list, target: int) -> tuple:
    # Generate all combinations of 3 elements from the list
    triplets = list(combinations(numbers, 3))

    # to check all the combinations
    # print(triplets)

    # Find the triplets whose sum is equals to the target
    matching_triplets = [triplet for triplet in triplets if sum(triplet) == target]

    return matching_triplets # This will return the list of matching triplets if any or an empty list if none found






print("\t\tOutputs")
print("\t\t-------\n")
sample_list = [10, 501, 37, 22, 100, 999, 87, 351]

print(f"Given list of numbers: {sample_list}")
#Q 1: output
even,odd = separate_even_odd(sample_list)
print(" Separate even & Odd numbers in a list: ")
print(f"Even Number: {even},\nOdd Numbers: {odd}")

#Q 2: output
primes = find_primes(sample_list)
print("\nQ2: Find prime number in a list: ")
print(f"Prime Numbers: {primes}")

#Q 4: output
num = 12345
print("\nQ4: Find Sum of First and Last Digit of an Integer: ")
print(f"Sun of first and last digit of {num} : {sum_first_and_last_digit(num)}")


#Q 5: output
print("\nQ5: Find Ways to Make Rs. 10 Using Given Coins: ")
coins = [1,2,5,10]
print(f"way to make Rs. 10 in Given Coins {coins} is {find_a_way_to_make_10(coins)}")
"""
ways_list, ways_dict = find_ways_to_make_10()
# Print the result
print("Number of ways to make Rs. 10:", len(ways_list))  # Total number of ways
print("Combinations of coins that make Rs. 10:", ways_list)  # List of combinations
print("Dictionary of combinations with counts:", ways_dict)  # Dictionary of combinations with their counts
"""

#Q 6: output
print("\nQ6: Find Duplicates in Three Lists: ")
duplicates = find_duplicates([1, 2, 3, 4], [2, 3, 5, 6], [3, 6, 2, 7])
print(f"Duplicates in three lists: {duplicates}")


#Q 7: output
print("\nQ7: Find the First Non-Repeating Element in a List: ")
print(f"First non-repeating element: {first_non_repeating([4, 5, 4, 3, 5, 6, 3, 8])}")

#Q 8: output
print("\nQ8: Find the Minimum Element in a Sorted List: ")
sorted_list = [10, 8, 2, 3, 1, 4, 5]
print(f"The minimum element in the sorted list is: {find_minimum(sorted_list)}")

#Q 9: output
print("\nQ9: Find a Triplet Whose Sum Equals a Given Value: ")
triplet = find_triplet_with_sum([10, 20, 30, 9, 15, 14], 59)
#triplet = find_triplet_with_sum([10, 5, 5, 20, 30, 9 , 11], 30)
print(f"Triplet with sum 59: {triplet}")
