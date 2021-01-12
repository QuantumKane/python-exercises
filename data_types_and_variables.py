
# 1. You have rented some movies for your kids. How much will you have to pay?

total_price = 0
daily_price = 3.00

l_mermaid = 3
bro_bear = 5
herc = 1

total_price = daily_price * (l_mermaid + bro_bear + herc)

# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. How much will you receive in payment for this week? 

weeks_pay = 0
goog_pay = 400
am_pay = 380
face_pay = 350

goog_hours = 6
am_hours = 4
face_hours = 10

weeks_pay = (goog_pay * goog_hours) + (am_pay * am_hours) + (face_pay * face_hours)

# 3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

is_not_full = True
no_schedule_conflict = True                                                                                     

if (is_not_full and no_schedule_conlict):
    print("you can enroll")
else:
    print("no go")
    
# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

has_not_expired = True
two_or_more = True
prem_member = True

if (two_or_more or prem_member) and has_not_expired;
    print("You get the product offer")
else:
    print("maybe next time")

# 5. Create a variable that holds a boolean value for each of the following conditions:
# a. the password must be at least 5 characters
at_least_five = True

# b. the username must be no more than 20 characters
max_twenty = True

# c. the password must not be the same as the username
pswd_same_as_user = False

