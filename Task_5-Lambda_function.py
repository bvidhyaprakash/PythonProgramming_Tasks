from functools import reduce
import datetime
"""
1. To filter out the people under 18 and map remaining people's name to a new list from given dictionaries
"""
def get_adult_names(people : list) -> list:
    adults = list(filter(lambda person: person['age'] >=18, people))
    names = list(map(lambda person : person['name'],adults))
    return names


"""
2. use reduce and lambda to calculate the product of all numbers
"""
def list_of_product(my_numbers_list : list) -> list:
    product = reduce(lambda x,y : x*y, my_numbers_list)
    return product



"""
3. List comprehension, list of square of even number
"""
def square_of_even_number(my_numbers : list) -> list:
    squares = [num**2 for num in my_numbers if(lambda n:n%2 ==0) (num)]
    return squares



"""
4. check given string is a number
"""
def check_for_number(string : list) -> list:
    check_number = lambda num : num.isdigit()
    result = [check_number(num) for num in string]
    return result

"""
5. To extract year, month and date from a date time object
"""
def extract_datetime(c_datetime):
    mydatetime = c_datetime
    currentDate = lambda dt : (dt.day, dt.month, dt.year)
    get_currentDate = currentDate(mydatetime)
    return get_currentDate

if __name__ == "__main__":
    print("Outputs")
    print("-------\n")

    # Q 1: output
    people_list = [
        {'name':'Vidhy', 'age':38},
        {'name': 'Nithya', 'age': 33},
        {'name': 'shastick', 'age': 2},
        {'name': 'keshika', 'age': 8}
    ]
    print(f"\nQ1: To get the adult names from the given list: {people_list}")
    print(get_adult_names(people_list))


    # Q 2: output
    my_numbers_list = [4, 5, 6, 7]
    print(f"\nQ2: To calculate the product of all numbers from the given list: {my_numbers_list}")
    print(list_of_product(my_numbers_list))


    # Q 3: output
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(f"\nQ3: To get the square of even number from the given list: {numbers}")
    print(square_of_even_number(numbers))

    # Q 4: output
    string_list = ['123', 'abc', '123.5', '12b']
    print(f"\nQ4: To check given string is a number from the given list: \n{string_list}")
    print(check_for_number(string_list))

  # Q 5: output
    current_datetime = datetime.datetime.now()
    print(f"\nQ5: To extract year, month and date from a date time object from the given date: \n{current_datetime}")
    print(extract_datetime(current_datetime))

