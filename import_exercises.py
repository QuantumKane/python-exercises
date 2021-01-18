/*
# 1. Import and test 3 of the functions from your functions exercise file.

*/

import function_exercises as fc
from function_exercises import capitalize_consonant
from function_exercises import calculate_tip as tip_calc

/*
# 2. Use the itertools module from the standard library to help you solve the problem.
*/

import itertools

print(itertools.permutations('abcd', 2))


/*
# 3. Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. 
*/

import json

profiles = open('profiles.json')
list_of_profiles = json.load(profiles)

/*
# 3-1. Total number of users
*/
total_users = len(list_of_profiles)

total_users

/* 
# 3-2. Active users
*/
active_users = len([user for user in list_of_profiles if user["isActive"]])

active_users

/*
# 3-3. Inactive users
*/
inactive_users = len([user for user in list_of_profiles if not user["isActive"]])

inactive_users

/*
# 3-4. Grand total of balances for all users
*/

def get_balance(dict):
    total = 0
    for user in list_of_profiles:
        balance = user['balance'].replace('$', '')
        balance = balance.replace(',', '')
        total += float(balance)
    return total

get_balance(list_of_profiles)

/*
# 3-5. Average balance per user
*/

def avg_balance(dict):
    total = 0
    for user in list_of_profiles:
        balance = user['balance'].replace('$', '')
        balance = balance.replace(',', '')
        total += float(balance)
    return round(total / len(list_of_profiles), 2)

avg_balance(list_of_profiles)

/*
# 3-6. User with the lowest balance
*/