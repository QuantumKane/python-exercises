{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (function_exercises.py, line 37)",
     "output_type": "error",
     "traceback": [
      "Traceback \u001b[0;36m(most recent call last)\u001b[0m:\n",
      "  File \u001b[1;32m\"/usr/local/anaconda3/lib/python3.7/site-packages/IPython/core/interactiveshell.py\"\u001b[0m, line \u001b[1;32m3326\u001b[0m, in \u001b[1;35mrun_code\u001b[0m\n    exec(code_obj, self.user_global_ns, self.user_ns)\n",
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-1-22d0ee2be0e1>\"\u001b[0;36m, line \u001b[0;32m3\u001b[0;36m, in \u001b[0;35m<module>\u001b[0;36m\u001b[0m\n\u001b[0;31m    from function_exercises import is_two\u001b[0m\n",
      "\u001b[0;36m  File \u001b[0;32m\"/Users/stevekane/codeup-data-science/python-exercises/function_exercises.py\"\u001b[0;36m, line \u001b[0;32m37\u001b[0m\n\u001b[0;31m    if is_consonant(first_letter):\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "# 1. Import and test 3 of the functions from your functions exercise file.\n",
    "\n",
    "from function_exercises import is_two"
   ]
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
