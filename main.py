
def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
  if b == 0: 
      raise ValueError("Cannot divide by zero.") 
  return a / b 

def is_even(number):
    return number % 2 == 0 

def factorial(n): 
    if n < 0: 
        raise ValueError("Factorial not defined for negative numbers") 
    if n == 0: 
        return 1 
    product = 1 
    for i in range(1, n + 1): 
        product *= i 
    return product 

def reverse_string(s): 
    return s[::-1] 

def is_palindrome(s): 
    return s == s[::-1] 

def find_min(lst): 
    if not lst: 
        raise ValueError("Empty list has no minimum value.") 
    min_val = lst[0] 
    for num in lst[1:]: 
        if num < min_val: 
            min_val = num 
    return min_val 

def count_occurrences(lst, target): 
    return lst.count(target) 

def remove_duplicates(lst): 
    return list(set(lst)) 

def fibonacci(n): 
    if n <= 0: 
        raise ValueError("Fibonacci not defined for non-positive integers.") 
    a, b = 0, 1 
    for _ in range(n - 1): 
        a, b = b, a + b 
    return a 

def sum_of_list(lst): 
    return sum(lst) 

def find_max(lst): 
    if not lst: 
        raise ValueError("Empty list has no maximum value.") 
    return max(lst) 

def average(lst): 
    if not lst: 
        raise ValueError("Cannot compute the average of an empty list.") 
    return sum(lst) / len(lst) 

def to_uppercase(s): 
    return s.upper() 

def get_even_numbers(lst): 
    return [num for num in lst if num % 2 == 0] 

def square(n): 
    return n ** 2 

def join_strings(string_list, separator): 
    return separator.join(string_list) 

def are_anagrams(s1, s2): 
    return sorted(s1) == sorted(s2) 

def to_snake_case(s): 
    return '_'.join(word.lower() for word in s.split()) 

def is_leap_year(year): 
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) 

def sum_of_squares(lst): 
    return sum(x**2 for x in lst) 

def replace_vowels(s, char): 
    return ''.join(char if c.lower() in 'aeiou' else c for c in s) 

from datetime import datetime 
def age_in_days(birthdate): 
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d") 
    today = datetime.now() 
    return (today - birthdate).days 

def gcd(a, b): 
    while b: 
        a, b = b, a % b 
    return a 

def second_largest(lst): 
    if len(lst) < 2: 
        return None 
    return sorted(set(lst))[-2] 

def generate_primes(n): 
    primes = [] 
    for possiblePrime in range(2, n+1): 
        isPrime = True 
        for num in range(2, int(possiblePrime ** 0.5) + 1): 
            if possiblePrime % num == 0: 
                isPrime = False 
                break 
        if isPrime: 
            primes.append(possiblePrime) 
    return primes 