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

# def second_conversion(minutes,hours):
#     return f"Conversion of {minutes} to Seconds is >> {minutes*60} || Conversion of Hours of {hours} to seconds is >> {hours*360}" 

def minutes_to_secounds(minutes):
    return minutes*60
print(minutes_to_secounds(5))

def hours_to_second(hours):
    return hours*minutes_to_secounds(60)

print(hours_to_second(1))

def seconds_in_a_day():
    return 24*hours_to_second(1)

print(seconds_in_a_day())

def seconds_in_month_august(days):
    return days*seconds_in_a_day()


def hours_in_a_month(days):
    return days*24
print(f"Hours in a june Month {hours_in_a_month(30)}")

def minutes_in_august(days):
    return  days*24*60
print(f"Minutes in August {minutes_in_august(31)}")

def minutes_in_year():
    
    days31_in_year =  minutes_in_august(31)
    days30_in_year = hours_in_a_month(30)*60
    days28_in_year = hours_in_a_month(28)*60
    print(days28_in_year)
    total_minutes = days31_in_year * 7  + days30_in_year * 4 + days28_in_year
    return f"Minutes in a year  : {total_minutes}"

print(minutes_in_year())
# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->

def mid(string_input):
    strlength = len(string_input)
    if strlength % 2 != 0:
        halfStr = strlength//2
        
        return string_input[halfStr]
        
    else:
        return ""
        
print(mid('hhAhh'))
print(mid('happpypppht'))
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
def hide_cc_number(cc_number):
    cc_length = len(cc_number)
    # print(cc_length)
    hidden_part =''
    for  x in range(cc_length - 4): 
        hidden_part += '*'
        print (hidden_part)
    visible_part = cc_number[-4:]
    card_number = hidden_part + visible_part
    print(card_number)
    
hide_cc_number("1234567890")
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
statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
 }

def online_count(directory):
    count = 0
    for key in directory:
        if directory[key] == 'online':
            count += 1
            
    return count
    
print(f"Online count : {online_count(statuses)}")
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
def discount_price(price,discount):
    
    result =  price - price*(discount)*0.01
    return result
print(f"Discount price : {discount_price(100,20)}")
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
import math
def hypotenouse_length(Adjacent,Opposite):
    
    result = math.sqrt(pow(Adjacent,2)+pow(Opposite,2))
    return result

print(f"Hypotenouse Length :{hypotenouse_length(10,15)}")
# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->

def fibonacci(f_num,s_num):
    fibonacci_array = [f_num,s_num]
    
    for x in range(9):
        result = fibonacci_array[-2] + fibonacci_array[-1]
        fibonacci_array.append(result)
        # print(fibonacci_array)
    return fibonacci_array
list = fibonacci(5,8)
print(f"Fibonacci Sequences : {list}")
# ---------------------------------
