# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

## - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
def minutes_to_seconds(minutes):
            return minutes * 60

minutes = 1
print(minutes_to_seconds(minutes))
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
def hours_to_seconds(hours):
            return hours * 3600

hours = 1
print(hours_to_seconds(hours))
# -  We're on the right track here, how many seconds are in a day
def seconds_in_a_day(seconds_per_hour):
            return seconds_per_hour * 24

seconds_per_hour = 60
print(seconds_in_a_day(seconds_per_hour))
# - How many Hours are in the month of June? 
def hours_in_june(hours):
            return hours * 31

hours = 24
print(hours_in_june(hours))            
# - How many Minutes are in the month of August?
def minutes_in_aug():
            print(60*24*30)        

minutes_in_aug()
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->

def mid(string):
    length = len(string)
    if length % 2 == 0:
            return string[length // 2 -1: length // 2 + 1]
    else:
            return string[length // 2]
    
input_string = "Mia"
print(mid(input_string))
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->

def hide_card_number(card_num):
        hidden_dig = len(card_num) -4
        return '*' * hidden_dig + card_num[-4:]

print(hide_card_number("8322381989"))
# ---------------------------------



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

"""
statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

"""

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings 
# of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.
        
# ---------------------------------
#      Solution Goes Here ->

def online_count(statuses):
        count = 0
        for status in statuses.values():
                if status == "online":
                        count += 1
        return count

statuses = {
        "Mia" : "online",
        "Michael" : "online",
        "Jax" : "offline"
}

print(online_count(statuses))
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.


# ---------------------------------
#      Solution Goes Here ->

def price(full_price, discount_perc):
        discounted_price = full_price - (full_price * discount_perc /100)
        return discounted_price

full_price = 10
discount_perc = 60
print(price(full_price, discount_perc))
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
