{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Conditional Basics\n",
    "\n",
    "#### a) Prompt the user for a day of the week, print out whether the day is Monday or not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "day_of_the_week = input('What is the day of the week?')\n",
    "if day_of_the_week == 'Monday':\n",
    "    print('Just another Manic Monday...')\n",
    "else:\n",
    "    print('Whew - not a Monday!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### b) Prompt the user for a day of the week, print out whether the day is a weekday or a weekend"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "is_weekend = input('Give me a day of the week')\n",
    "if is_weekend == 'Saturday':\n",
    "    print('Welcome to the weekend!')\n",
    "elif is_weekend == 'Sunday':\n",
    "    print('Welcome to the weekend!')\n",
    "else:\n",
    "    print('...Miles to go before I sleep')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### c) Create variables and make up values for:\n",
    "- the number of hours worked in one week\n",
    "- the hourly rate\n",
    "- how much the week's paycheck will be\n",
    "#### Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This week's paycheck is 717.0\n"
     ]
    }
   ],
   "source": [
    "num_of_hours = float(45.2)\n",
    "hourly_rate = float(15.0)\n",
    "paycheck = float(0)\n",
    "\n",
    "if num_of_hours <= 40:\n",
    "    paycheck = num_of_hours * hourly_rate\n",
    "elif num_of_hours > 40:\n",
    "    paycheck = ((num_of_hours - 40) * hourly_rate * 1.5) + hourly_rate * 40\n",
    "    print(f\"This week\\'s paycheck is {paycheck}\")    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Loop Basics\n",
    "#### a) While\n",
    "- Create an integer variable i with a value of 5.\n",
    "- Create a while loop that runs so long as i is less than or equal to 15\n",
    "- Each loop iteration, output the current value of i, then increment i by one."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "i = 5\n",
    "\n",
    "while i <= 15:\n",
    "    print(i)\n",
    "    i += 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### a2) Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "i = 0\n",
    "\n",
    "while i <= 100:\n",
    "    print(i)\n",
    "    i += 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### a3) Alter your loop to count backwards by 5's from 100 to -10."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n",
      "0\n",
      "-5\n",
      "-10\n"
     ]
    }
   ],
   "source": [
    "i = 100\n",
    "\n",
    "while i >= -10:\n",
    "    print(i)\n",
    "    i -= 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### a4) Create a while loop that starts at 2,and displays the number squared on each line while the number is less than 1,000,000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "16\n",
      "256\n",
      "65536\n"
     ]
    }
   ],
   "source": [
    "i = 2\n",
    "\n",
    "while i <= 1_000_000:\n",
    "    print(i)\n",
    "    i = i ** 2\n",
    "#   i *= i"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### a5) Write a loop that uses print to create the output shown below"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "i = 100\n",
    "\n",
    "while i >= 5:\n",
    "    print(i)\n",
    "    i -= 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### b) For Loops\n",
    "- Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9 x 1 = 9\n",
      "9 x 2 = 18\n",
      "9 x 3 = 27\n",
      "9 x 4 = 36\n",
      "9 x 5 = 45\n",
      "9 x 6 = 54\n",
      "9 x 7 = 63\n",
      "9 x 8 = 72\n",
      "9 x 9 = 81\n",
      "9 x 10 = 90\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "\n",
    "for i in range(1, 11):\n",
    "   print(num, \"x\", i, \"=\", num * i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### b2) Create a for loop that uses print to create the output shown below.\n",
    "1\n",
    "22\n",
    "333\n",
    "4444\n",
    "55555\n",
    "666666\n",
    "7777777\n",
    "88888888\n",
    "999999999"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "22\n",
      "333\n",
      "4444\n",
      "55555\n",
      "666666\n",
      "7777777\n",
      "88888888\n",
      "999999999\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 10):\n",
    "    print(str(i) * i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### c) Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter an odd number between 1 and 50: 2\n",
      "Enter an odd number between 1 and 50: 23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here is an odd number: 1\n",
      "Here is an odd number: 3\n",
      "Here is an odd number: 5\n",
      "Here is an odd number: 7\n",
      "Here is an odd number: 9\n",
      "Here is an odd number: 11\n",
      "Here is an odd number: 13\n",
      "Here is an odd number: 15\n",
      "Here is an odd number: 17\n",
      "Here is an odd number: 19\n",
      "Here is an odd number: 21\n",
      "Gotcha! Skipping number:  23\n",
      "Here is an odd number: 25\n",
      "Here is an odd number: 27\n",
      "Here is an odd number: 29\n",
      "Here is an odd number: 31\n",
      "Here is an odd number: 33\n",
      "Here is an odd number: 35\n",
      "Here is an odd number: 37\n",
      "Here is an odd number: 39\n",
      "Here is an odd number: 41\n",
      "Here is an odd number: 43\n",
      "Here is an odd number: 45\n",
      "Here is an odd number: 47\n",
      "Here is an odd number: 49\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    odd_num = input('Enter an odd number between 1 and 50:')\n",
    "    if odd_num.isdigit():\n",
    "        odd_num = int(odd_num)\n",
    "        if odd_num % 2 == 0:\n",
    "            continue\n",
    "        break\n",
    "               \n",
    "num = 1\n",
    "while num <= 50:\n",
    "    if num == odd_num:\n",
    "        print('Gotcha! Skipping number: ', num)\n",
    "        num += 2\n",
    "        continue\n",
    "       \n",
    "    print('Here is an odd number:', num)\n",
    "    num += 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### d) Prompt the user to enter a positive number and write a loop that counts from 0 to that number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a positive number greater than zero  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    pos_num = input('Enter a positive number greater than zero: ')\n",
    "    if pos_num.isdigit():\n",
    "        pos_num = int(pos_num)\n",
    "        if pos_num <= 0:\n",
    "            continue\n",
    "        break\n",
    "        \n",
    "num = 0\n",
    "while num <= pos_num:\n",
    "    print(num)\n",
    "    num += 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### e) Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a positive number greater than zero:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    pos_num = input('Enter a positive number greater than zero: ')\n",
    "    if pos_num.isdigit():\n",
    "        pos_num = int(pos_num)\n",
    "        if pos_num <= 0:\n",
    "            continue\n",
    "        break\n",
    "while pos_num > 0:\n",
    "    print(pos_num)\n",
    "    pos_num -= 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3. Fizzbuzz\n",
    " - Write a program that prints the numbers from 1 to 100.\n",
    " - For multiples of three print \"Fizz\" instead of the number\n",
    " - For the multiples of five print \"Buzz\".\n",
    " - For numbers which are multiples of both three and five print \"FizzBuzz\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "5 Buzz\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "10 Buzz\n",
      "11\n",
      "Fizz\n",
      "13\n",
      "14\n",
      "15 Fizzbuzz\n",
      "16\n",
      "17\n",
      "Fizz\n",
      "19\n",
      "20 Buzz\n",
      "Fizz\n",
      "22\n",
      "23\n",
      "Fizz\n",
      "25 Buzz\n",
      "26\n",
      "Fizz\n",
      "28\n",
      "29\n",
      "30 Fizzbuzz\n",
      "31\n",
      "32\n",
      "Fizz\n",
      "34\n",
      "35 Buzz\n",
      "Fizz\n",
      "37\n",
      "38\n",
      "Fizz\n",
      "40 Buzz\n",
      "41\n",
      "Fizz\n",
      "43\n",
      "44\n",
      "45 Fizzbuzz\n",
      "46\n",
      "47\n",
      "Fizz\n",
      "49\n",
      "50 Buzz\n",
      "Fizz\n",
      "52\n",
      "53\n",
      "Fizz\n",
      "55 Buzz\n",
      "56\n",
      "Fizz\n",
      "58\n",
      "59\n",
      "60 Fizzbuzz\n",
      "61\n",
      "62\n",
      "Fizz\n",
      "64\n",
      "65 Buzz\n",
      "Fizz\n",
      "67\n",
      "68\n",
      "Fizz\n",
      "70 Buzz\n",
      "71\n",
      "Fizz\n",
      "73\n",
      "74\n",
      "75 Fizzbuzz\n",
      "76\n",
      "77\n",
      "Fizz\n",
      "79\n",
      "80 Buzz\n",
      "Fizz\n",
      "82\n",
      "83\n",
      "Fizz\n",
      "85 Buzz\n",
      "86\n",
      "Fizz\n",
      "88\n",
      "89\n",
      "90 Fizzbuzz\n",
      "91\n",
      "92\n",
      "Fizz\n",
      "94\n",
      "95 Buzz\n",
      "Fizz\n",
      "97\n",
      "98\n",
      "Fizz\n",
      "100 Buzz\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 101):\n",
    "        if i % 5 == 0 and i % 3 == 0:\n",
    "            print(i, 'Fizzbuzz')\n",
    "        elif i % 3 == 0:\n",
    "            print('Fizz') # ONLY 'fizz' per instuctions\n",
    "        elif i % 5 == 0:\n",
    "            print (i, 'Buzz')\n",
    "        else: \n",
    "            print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4. Display a table of powers.\n",
    "\n",
    " - Prompt the user to enter an integer.\n",
    " - Display a table of squares and cubes from 1 to the value entered.\n",
    " - Ask if the user wants to continue.\n",
    " - Assume that the user will enter valid data.\n",
    " - Only continue if the user agrees to."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter an integer 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number | squared | cubed\n",
      "------ | ------- | -----\n",
      "     1 |       1 |     1\n",
      "     2 |       4 |     8\n",
      "     3 |       9 |    27\n",
      "     4 |      16 |    64\n",
      "     5 |      25 |   125\n",
      "     6 |      36 |   216\n"
     ]
    }
   ],
   "source": [
    "# Zach's solution\n",
    "\n",
    "user_num = int(input('Enter an integer'))\n",
    "\n",
    "print('number | squared | cubed')\n",
    "print('------ | ------- | -----')\n",
    "for i in range(1, user_num + 1):\n",
    "    print('%6d | %7d | %5d' % (i, i**2, i**3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 5. Convert given number grades into letter grades.\n",
    "\n",
    " - Prompt the user for a numerical grade from 0 to 100.\n",
    " - Display the corresponding letter grade.\n",
    " - Prompt the user to continue.\n",
    " - Assume that the user will enter valid integers for the grades.\n",
    " - The application should only continue if the user agrees to. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number grade:  45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "F\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to continue?  y\n",
      "Enter a number grade:  444\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to continue?  yea\n",
      "Enter a number grade:  88\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to continue?  n\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    numeric_grade = int(input(\"Enter a number grade: \"))\n",
    "\n",
    "    if numeric_grade >= 88:\n",
    "        print(\"A\")\n",
    "    elif numeric_grade >= 80:\n",
    "        print(\"B\")\n",
    "    elif numeric_grade >= 67:\n",
    "        print(\"C\")\n",
    "    elif numeric_grade >= 60:\n",
    "        print(\"D\")\n",
    "    else: \n",
    "        print(\"F\")\n",
    "        \n",
    "    continue_input = input(\"Do you want to continue? \")\n",
    "    if not continue_input.lower().startswith(\"y\"):\n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Dune', 'author': 'Frank Herbert', 'genre': 'Science Fiction'},\n",
       " {'title': \"Lord Foul's Bane\",\n",
       "  'author': 'Stephen R Donaldson',\n",
       "  'genre': 'Fantasy'},\n",
       " {'title': 'The Great Shark Hunt',\n",
       "  'author': 'Hunter S Thompson',\n",
       "  'genre': 'Journalism'},\n",
       " {'title': 'God Emperor of Dune',\n",
       "  'author': 'Frank Herbert',\n",
       "  'genre': 'Science Fiction'}]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "books = [\n",
    "    {\"title\": \"Dune\", \"author\": \"Frank Herbert\", \"genre\": \"Science Fiction\"},\n",
    "    {\"title\": \"Lord Foul's Bane\", \"author\": \"Stephen R Donaldson\", \"genre\": \"Fantasy\"},\n",
    "    {\"title\": \"The Great Shark Hunt\", \"author\": \"Hunter S Thompson\", \"genre\": \"Journalism\"},\n",
    "    {\"title\": \"God Emperor of Dune\", \"author\": \"Frank Herbert\", \"genre\": \"Science Fiction\"}\n",
    "]\n",
    "\n",
    "list(books)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 6a) Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a genre:  Fantasy\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------\n",
      "Title: Lord Foul's Bane\n",
      "Author: Stephen R Donaldson\n",
      "Genre: Fantasy\n",
      "--------------\n",
      "Title: The Hobbit\n",
      "Author: JRR Tolkien\n",
      "Genre: Fantasy\n"
     ]
    }
   ],
   "source": [
    "books = [\n",
    "    {\"title\": \"Dune\", \"author\": \"Frank Herbert\", \"genre\": \"Science Fiction\"},\n",
    "    {\"title\": \"Lord Foul's Bane\", \"author\": \"Stephen R Donaldson\", \"genre\": \"Fantasy\"},\n",
    "    {\"title\": \"The Great Shark Hunt\", \"author\": \"Hunter S Thompson\", \"genre\": \"Journalism\"},\n",
    "    {\"title\": \"The Hobbit\", \"author\": \"JRR Tolkien\", \"genre\": \"Fantasy\"},\n",
    "    {\"title\": \"God Emperor of Dune\", \"author\": \"Frank Herbert\", \"genre\": \"Science Fiction\"}\n",
    "]\n",
    "\n",
    "select_genre = input(\"Enter a genre: \")\n",
    "select_books = [book for book in books if book['genre'] == select_genre]\n",
    "\n",
    "for book in select_books:\n",
    "    print(\"--------------\")\n",
    "    print(f\"Title: {book['title']}\")\n",
    "    print(f\"Author: {book['author']}\")\n",
    "    print(f\"Genre: {book['genre']}\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
