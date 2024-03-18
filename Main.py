# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
#      Solution Goes Here ->

# convert minutes to seconds
def minutes_to_seconds(minutes):
    print(minutes * 60)

minutes_to_seconds(1)
minutes_to_seconds(5)

# convent hours into seconds
def time_to_seconds(time, unit='mintues'):
    if unit == 'hours':
        time *= 60
    return time * 60

print(time_to_seconds(1, 'mintues'))
print(time_to_seconds(5, 'mintues'))
print(time_to_seconds(1, 'hours'))
print(time_to_seconds(2, 'hours'))

# seconds in a day
seconds_in_a_day = 24 * 60 * 60
print("Number of seconds in a day:", seconds_in_a_day)

# hours in the month of June
days_in_june = 30
hours_in_a_day = 24
hours_in_june = days_in_june * hours_in_a_day
print("Number of hours in the month of June:", hours_in_june)

# minutes in the month of August
days_in_august = 31
hours_in_a_day = 24
minutes_in_an_hour = 60
minutes_in_august = days_in_august * hours_in_a_day * minutes_in_an_hour
print("Number of minutes in the month of August:", minutes_in_august)

# Bouns #1 - Minutes in a year
days_in_non_leap_year = 365
days_in_leap_year = 366
hours_in_a_day = 24
minutes_in_an_hour = 60
minutes_in_non_leap_year = days_in_non_leap_year * hours_in_a_day * minutes_in_an_hour
minutes_in_leap_year = days_in_leap_year * hours_in_a_day * minutes_in_an_hour
minutes_in_a_year = (minutes_in_non_leap_year + minutes_in_leap_year) / 2
print("Number of minutes in a year (on average):", minutes_in_a_year)
# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
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
