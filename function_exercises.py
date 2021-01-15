{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1. Define a function named is_two. It should accept one input and return True \n",
    "# if the passed input is either the number or the string 2\n",
    "# structure: int -> boolean\n",
    "\n",
    "def is_two(number):\n",
    "    if int(number) == 2:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "is_two(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 2. Define a function named is_vowel. It should return True if the passed \n",
    "# string is a vowel, False otherwise.\n",
    "\n",
    "def is_vowel(string):\n",
    "    return any(vowel in string.lower() for vowel in 'aeiou')\n",
    "    \n",
    "is_vowel('rrr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-22-16ac8fa340cd>, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-22-16ac8fa340cd>\"\u001b[0;36m, line \u001b[0;32m5\u001b[0m\n\u001b[0;31m    return any(letter in string.lower() for letter not 'aeiou')\u001b[0m\n\u001b[0m                                                     ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "# 3. Define a function named is_consonant. It should return True if the passed string\n",
    "# is a consonant, False otherwise. Use your is_vowel function to accomplish this.\n",
    "\n",
    "def is_consonant(string):\n",
    "     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. Define a function that accepts a string that is a word. The function should \n",
    "# capitalize the first letter of the word if the word starts with a consonant.\n",
    "\n",
    "def capitalize_consonant(string):\n",
    "    if \n",
    "    return \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.0"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 5. Define a function named calculate_tip. It should accept a tip percentage \n",
    "# (a number between 0 and 1) and the bill total, and return the amount to tip.\n",
    "\n",
    "def calculate_tip(bill):\n",
    "    tip = float(bill) * .20\n",
    "    return tip\n",
    "\n",
    "calculate_tip(25.00)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.5"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 6. Define a function named apply_discount. It should accept a original price, \n",
    "# and a discount percentage, and return the price after the discount is applied.\n",
    "\n",
    "def apply_discount(original_price):\n",
    "    discounted_price = float(original_price) * .10\n",
    "    return discounted_price\n",
    "\n",
    "apply_discount(25.00)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000000"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 7. Define a function named handle_commas. It should accept a string that is a \n",
    "# number that contains commas in it as input, and return a number as output.\n",
    "\n",
    "def handle_commas(input):\n",
    "    input = input.replace(',', '')\n",
    "    return int(input)\n",
    "\n",
    "handle_commas('1,000,000')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'A'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 8. Define a function named Define a function named get_letter_grade. It should \n",
    "# accept a number and return the letter grade associated with that number (A-F).\n",
    "\n",
    "def get_letter_grade(numeric_grade):\n",
    "    \n",
    "        if numeric_grade >= 88:\n",
    "            return(\"A\")\n",
    "        elif numeric_grade >= 80:\n",
    "            return(\"B\")\n",
    "        elif numeric_grade >= 67:\n",
    "            return(\"C\")\n",
    "        elif numeric_grade >= 60:\n",
    "            return(\"D\")\n",
    "        else: \n",
    "            return(\"F\")\n",
    "\n",
    "get_letter_grade(88)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'cptl'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 9. Define a function named remove_vowels that accepts a string and returns a \n",
    "# string with all the vowels removed.\n",
    "\n",
    "def remove_vowels(string):\n",
    "    vowels = 'aeiouAEIOU'\n",
    "    return \"\".join([letter for letter in string if letter not in vowels])\n",
    "\n",
    "remove_vowels('capital')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'steve_kane'"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 10. Define a function named normalize_name. It should accept a string and return a \n",
    "# valid python identifier, that is:\n",
    "# - anything that is not a valid python identifier should be removed\n",
    "# - leading and trailing whitespace should be removed\n",
    "# - everything should be lowercase\n",
    "# - spaces should be replaced with underscores\n",
    "\n",
    "def normalize_name(name):\n",
    "    \n",
    "    name = name.strip()\n",
    "    name = name.lower()\n",
    "    name = name.replace(' ', '_')\n",
    "    \n",
    "    \n",
    "    if name.isidentifier() == True:\n",
    "        return name\n",
    "\n",
    "normalize_name('    Steve Kane ')"
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
