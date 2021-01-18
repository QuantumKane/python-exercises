# 1. Conditional Basics

# a) Prompt the user for a day of the week, print out whether the day is Monday or not

day_of_the_week = input('What is the day of the week?')
if day_of_the_week == 'Monday':
    print('Just another Manic Monday...')
else:
    print('Whew - not a Monday!')
    
# b) Prompt the user for a day of the week, print out whether the day is a weekday or a weekend

is_weekend = input('Give me a day of the week')
if is_weekend == 'Saturday':
    print('Welcome to the weekend!')
elif is_weekend == 'Sunday':
    print('Welcome to the weekend!')
else:
    print('...Miles to go before I sleep')
    
    
# c) Create variables and make up values for:
- the number of hours worked in one week
- the hourly rate
- how much the week's paycheck will be
# Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

num_of_hours = float(45.2)
hourly_rate = float(15.0)
paycheck = float(0)

if num_of_hours <= 40:
    paycheck = num_of_hours * hourly_rate
elif num_of_hours > 40:
    paycheck = ((num_of_hours - 40) * hourly_rate * 1.5) + hourly_rate * 40
    print(f"This week\'s paycheck is {paycheck}")
    
# Loop Basics
# a) While
- Create an integer variable i with a value of 5.
- Create a while loop that runs so long as i is less than or equal to 15
- Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i += 1
    
# a2) Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0

while i <= 100:
    print(i)
    i += 2
    
# a3) Alter your loop to count backwards by 5's from 100 to -10.

i = 100

while i >= -10:
    print(i)
    i -= 5
    
# a4) Create a while loop that starts at 2,and displays the number squared on each line while the number is less than 1,000,000

i = 2

while i <= 1_000_000:
    print(i)
    i = i ** 2
    
# a5) Write a loop that uses print to create the output shown belowi = 100

while i >= 5:
    print(i)
    i -= 5
    
# b) For Loops
- Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number

num = int(input("Enter a number: "))

for i in range(1, 11):
   print(num, "x", i, "=", num * i)
   
   
# b2) Create a for loop that uses print to create the output shown below.

for i in range(1, 10):
    print(str(i) * i)
    
# c) Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.


while True:
    odd_num = input('Enter an odd number between 1 and 50:')
    if odd_num.isdigit():
        odd_num = int(odd_num)
        if odd_num % 2 == 0:
            continue
        break
               
num = 1
while num <= 50:
    if num == odd_num:
        print('Gotcha! Skipping number: ', num)
        num += 2
        continue
       
    print('Here is an odd number:', num)
    num += 2
    
# d) Prompt the user to enter a positive number and write a loop that counts from 0 to that number.

while True:
    pos_num = input('Enter a positive number greater than zero: ')
    if pos_num.isdigit():
        pos_num = int(pos_num)
        if pos_num <= 0:
            continue
        break
        
num = 0
while num <= pos_num:
    print(num)
    num += 1
    
# e) Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

while True:
    pos_num = input('Enter a positive number greater than zero: ')
    if pos_num.isdigit():
        pos_num = int(pos_num)
        if pos_num <= 0:
            continue
        break
while pos_num > 0:
    print(pos_num)
    pos_num -= 1
    
# 3. Fizzbuzz
 - Write a program that prints the numbers from 1 to 100.
 - For multiples of three print "Fizz" instead of the number
 - For the multiples of five print "Buzz".
 - For numbers which are multiples of both three and five print "FizzBuzz".
 
 
for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print(i, 'Fizzbuzz')
        elif i % 3 == 0:
            print('Fizz') # ONLY 'fizz' per instuctions
        elif i % 5 == 0:
            print (i, 'Buzz')
        else: 
            print(i)
            
# 4. Display a table of powers.

 - Prompt the user to enter an integer.
 - Display a table of squares and cubes from 1 to the value entered.
 - Ask if the user wants to continue.
 - Assume that the user will enter valid data.
 - Only continue if the user agrees to. 
 
# Zach's solution

user_num = int(input('Enter an integer'))

print('number | squared | cubed')
print('------ | ------- | -----')
for i in range(1, user_num + 1):
    print('%6d | %7d | %5d' % (i, i**2, i**3))
    
    
# 5. Convert given number grades into letter grades.

 - Prompt the user for a numerical grade from 0 to 100.
 - Display the corresponding letter grade.
 - Prompt the user to continue.
 - Assume that the user will enter valid integers for the grades.
 - The application should only continue if the user agrees to. 
 
 
while True:
    numeric_grade = int(input("Enter a number grade: "))

    if numeric_grade >= 88:
        print("A")
    elif numeric_grade >= 80:
        print("B")
    elif numeric_grade >= 67:
        print("C")
    elif numeric_grade >= 60:
        print("D")
    else: 
        print("F")
        
    continue_input = input("Do you want to continue? ")
    if not continue_input.lower().startswith("y"):
        break
        
        
# 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.


books = [
    {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction"},
    {"title": "Lord Foul's Bane", "author": "Stephen R Donaldson", "genre": "Fantasy"},
    {"title": "The Great Shark Hunt", "author": "Hunter S Thompson", "genre": "Journalism"},
    {"title": "God Emperor of Dune", "author": "Frank Herbert", "genre": "Science Fiction"}
]

list(books)

# 6a) Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.


books = [
    {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction"},
    {"title": "Lord Foul's Bane", "author": "Stephen R Donaldson", "genre": "Fantasy"},
    {"title": "The Great Shark Hunt", "author": "Hunter S Thompson", "genre": "Journalism"},
    {"title": "The Hobbit", "author": "JRR Tolkien", "genre": "Fantasy"},
    {"title": "God Emperor of Dune", "author": "Frank Herbert", "genre": "Science Fiction"}
]

select_genre = input("Enter a genre: ")
select_books = [book for book in books if book['genre'] == select_genre]

for book in select_books:
    print("--------------")
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Genre: {book['genre']}")