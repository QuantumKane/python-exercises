{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Import and test 3 of the functions from your functions exercise file.\n",
    "\n",
    "import function_exercises as fc\n",
    "from function_exercises import capitalize_consonant\n",
    "from function_exercises import calculate_tip as tip_calc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fc.is_two(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fc.is_vowel('A')"
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
       "True"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fc.is_consonant('C')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Steve'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "capitalize_consonant('steve')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12.5"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tip_calc(.25, 50)"
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
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import itertools"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(itertools.permutations('abcd', 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "profiles = open('profiles.json')\n",
    "list_of_profiles = json.load(profiles)\n",
    "list_of_profiles[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#1. Number of users\n",
    "\n",
    "total_users = len(list_of_profiles)\n",
    "total_users"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Active users\n",
    "\n",
    "active_users = len([user for user in list_of_profiles if user[\"isActive\"]])\n",
    "active_users"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list_of_profiles[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3. Inactive users\n",
    "\n",
    "inactive_users = len([user for user in list_of_profiles if not user[\"isActive\"]])\n",
    "inactive_users"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. Grand total of balances for all users\n",
    "\n",
    "def get_balance(dict):\n",
    "    total = 0\n",
    "    for user in list_of_profiles:\n",
    "        balance = user['balance'].replace('$', '')\n",
    "        balance = balance.replace(',', '')\n",
    "        total += float(balance)\n",
    "    return total"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_balance1(dict):\n",
    "    total = 0\n",
    "    for user in list_of_profiles:\n",
    "        total += float(user['balance'].replace('$', '').replace(',', ''))\n",
    "    return total"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "get_balance(list_of_profiles)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Average balance per user\n",
    "\n",
    "def avg_balance(dict):\n",
    "    total = 0\n",
    "    for user in list_of_profiles:\n",
    "        balance = user['balance'].replace('$', '')\n",
    "        balance = balance.replace(',', '')\n",
    "        total += float(balance)\n",
    "    return round(total / len(list_of_profiles), 2)\n",
    "\n",
    "avg_balance(list_of_profiles)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 6. User with the lowest balance\n",
    "\n",
    "def min_balance(dict):\n",
    "    balances = []\n",
    "    for user in list_of_profiles:\n",
    "        balance = user['balance'].replace('$', '')\n",
    "        balance = float(balance.replace(',', ''))\n",
    "        balances.append(balance)\n",
    "    \n",
    "        \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "min()"
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
