
# 1. You have rented some movies for your kids. How much will you have to pay?

total_price = 0
daily_price = 3.00

l_mermaid_days = 3
bro_bear_days = 5
herc_days = 1

total_price = daily_price * (l_mermaid_days + bro_bear_days + herc_days)

# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. How much will you receive in payment for this week? 

weeks_pay = 0
google_pay = 400
amazon_pay = 380
facebook_pay = 350

google_hours = 6
amazon_hours = 4
facebook_hours = 10

weeks_pay = (google_pay * google_hours) + (amazon_pay * amazon_hours) + (facebook_pay * facebook_hours)

# 3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

is_not_full = True
no_schedule_conflict = True                                                                                     

if (is_not_full and no_schedule_conlict):
    print("You can enroll")
else:
    print("No go")
    
# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

has_not_expired = True
more_than_two = True
prem_member = True

if (more_than_two or prem_member) and has_not_expired;
    print("You get the product offer")
else:
    print("Maybe next time")

# 5. Create a variable that holds a boolean value for each of the following conditions:
# a. the password must be at least 5 characters
at_least_five = len(password) >= 5

# b. the username must be no more than 20 characters
max_twenty = len(username) <= 20

# c. the password must not be the same as the username
pswd_diff_from_user = password != username


# LIST COMPREHENSION EXERCISES

# 1. Make a variable named uppercased_fruits to hold the output
uppercased_fruits = [fruit.upper() for fruit in fruits]

# 2. Make a variable named capitalized_fruits
capitalized_fruits = [fruit.title() for fruit in fruits]

# 3. Make a variable named fruits_with_more_than_two_vowels
def count_vowels(string):
    count = 0
    for element in string:
        if element.lower() in ('aeiou'):
            count += 1
    return count

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) > 2]
fruits_with_more_than_two_vowels

# 4. Make a variable named fruits_with_only_two_vowels
fruits_with_only_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) == 2]

# 5. Make a list that contains each fruit with more than 5 characters
more_than_five = [fruit for fruit in fruits if (len(fruit) > 5)]

# 6. Make a list that contains each fruit with exactly 5 characters
exactly_five = [fruit for fruit in fruits where (len(fruit) == 5)]

# 7. Make a list that contains fruits that have less than 5 characters

less_than_five = [fruit for fruit in fruits if (len(fruit) < 5)]

# 8. Make a list containing the number of characters in each fruit.
char_count = [len(fruit) for fruit in fruits]

# 9. Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = 