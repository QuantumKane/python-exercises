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
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a positive number greater than zero 26\n"
     ]
    }
   ],
   "source": [
    "pos_num = int(input('Enter a positive number greater than zero'))"
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
