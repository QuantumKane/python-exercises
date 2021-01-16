"""
1. Define a function named is_two. It should accept one input and return True 
if the passed input is either the number or the string 2
signature: anything -> boolean
"""

def is_two(number):
    if int(number) == 2:
        return True
    else:
        return False
"""   
2. Define a function named is_vowel. It should return True if the passed 
string is a vowel, False otherwise.
signature: string -> boolean
""" 

def is_vowel(string):
    return any(vowel in string.lower() for vowel in 'aeiou')

"""
3. Define a function named is_consonant. It should return True if the passed string
is a consonant, False otherwise. Use your is_vowel function to accomplish this.
signature: str -> boolean
"""
def is_consonant(string):
     return string.isalpha() and not is_vowel(string)
    
"""
4. Define a function that accepts a string that is a word. The function should 
capitalize the first letter of the word if the word starts with a consonant.
signature string -> string
"""

def capitalize_consonant(word):
    first_letter = word[0]
       if is_consonant(first_letter):
           return word.capitalize()
       else:
           return word
    
"""
5. Define a function named calculate_tip. It should accept a tip percentage 
(a number between 0 and 1) and the bill total, and return the amount to tip.
Signature: (percentage: float, bill: float) -> float
"""

def calculate_tip(percentage, bill):
    tip = float(percentage) * float(bill) 
    return tip

"""
6. Define a function named apply_discount. It should accept a original price, 
and a discount percentage, and return the price after the discount is applied.
Signature: original_price:float -> float
"""

def apply_discount(original_price):
    discounted_price = float(original_price) * .10
    return original_price - discounted_price

"""
7. Define a function named handle_commas. It should accept a string that is a 
number that contains commas in it as input, and return a number as output.
signature: str -> float
"""

def handle_commas(input):
    input = input.replace(',', '')
    return int(input)

"""
8. Define a function named Define a function named get_letter_grade. It should 
accept a number and return the letter grade associated with that number (A-F).
signature: grade:float -> str
"""

def get_letter_grade(numeric_grade):
    
        if numeric_grade >= 90:
            return("A")
        elif numeric_grade >= 80:
            return("B")
        elif numeric_grade >= 70:
            return("C")
        elif numeric_grade >= 60:
            return("D")
        else: 
            return("F")

"""
9. Define a function named remove_vowels that accepts a string and returns a 
string with all the vowels removed.
signature: str -> str
"""

def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return "".join([letter for letter in string if letter not in vowels])

"""
10. Define a function named normalize_name. It should accept a string and return a 
valid python identifier, that is:
- anything that is not a valid python identifier should be removed
- leading and trailing whitespace should be removed
- everything should be lowercase
- spaces should be replaced with underscores
Signature: str -> str 
"""

def normalize_name(name):
    
    name = name.strip()
    name = name.lower()
    name = name.replace(' ', '_')
    
    if name.isidentifier() == True:
        return name
    
"""
11. Write a function named cumulative_sum that accepts a list of numbers and returns 
a list that is the cumulative sum of the numbers in the list.
signature: list -> list
"""

def cumulative_sum(list):
    
    sum = [list[0]]
    
    for n in list [1:]:
        prev_total = sum[-1]
        sum.append(prev_total + n)
    return sum

