
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
def sec_convert_from_min (min):
    return(min * 60)
sec_convert_from_min(1)

def sec_convert_from_hour (hour):
    return(hour * 3600)
sec_convert_from_hour(1)

sec_in_day = sec_convert_from_hour(24)
days_in_june = 30
days_in_august = 31

hours_in_june = sec_convert_from_hour(days_in_june)
minutes_in_august = (sec_convert_from_hour(24) * days_in_august) / 60

print(f'1) There are {sec_in_day} hours in a day. The month of June has {hours_in_june} hours. August has {minutes_in_august} minutes in the entire month.')

# ---------------------------------

#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->
import math 
#ref: https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number

def mid(string):
    string_length = len(string)
    if string_length % 2 == 0:
        return ""
    else:
        middle_after = math.ceil(string_length / 2)
        middle_index = middle_after - 1 
        
    return string[middle_index]
mid("Stephanie")
print(f'2) The letter in the middle of the name "Stephanie" is "{mid("Stephanie")}"')

# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
def hide_cc_num(cc_num):
    cc_num_input = []
    cc_num_input.append(cc_num)
    return(cc_num_input) 
    # top_range = len(cc_num) + 1
    # return(top_range)
print(hide_cc_num(123))
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
