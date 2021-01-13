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
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What is the day of the week? Monday\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Just another Manic Monday...\n"
     ]
    }
   ],
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
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Give me a day of the week Sunday\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wecome to the weekend!\n"
     ]
    }
   ],
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
    "#### c)"
   ]
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
