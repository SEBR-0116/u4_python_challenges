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
# ---------------------------------

def convert_to_seconds(unit):
  seconds = unit * 60;
  hours = unit * 3600;
  days = hours * 24;
  month_of_june = days * 30;
  month_of_august = days * 31;
  # print(seconds)
  # print(month_of_june)

# convert_to_seconds(1)

#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def mid(str):
  if len(str) % 2 == 0:
    print('')
  else: 
    middle = int(len(str)/2)
    print(str[middle])

# mid('abc')

# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def show_last_four(num):
  last_four = num[-4:]
  replace_num = len(num[:-4])
  num = num.replace(num[:-4], "*" * replace_num)
  print (num)

# show_last_four('123456789')


# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def online_count(dict):
  # take in a dictionary 
  count = 0
  for el in dict.values():
    if el == 'online':
      count += 1
  # return num of ppl online
  print(count)
  
# online_count(statuses)

#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def discount_price(full, disc_percentage):
  # return 
  # 100 - 100 * 20%
  new_price = full - full * disc_percentage * 0.01
  print(new_price)

# discount_price(100, 30)

#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
import math
def hypotenouse(opposite, adjacent):
  print(math.hypot(opposite, adjacent))

# hypotenouse(2, 2)

#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes one number and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def fibonacci(num1, num2):
  count = 0
  while count < 9:
    count += 1
    print(num1, num2)
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3



  # count = 0
  # num_arr = []

  # while count<9:
  #   while num < 3 and 0 <= num:
  #     num_arr.append(num)
  #     print(num)
  #     num +=1
  #     count += 1
  
  #   count += 1

  #   num = (num-1) + (num-2)
  #   print('count is',count)
  #   print(num)

fibonacci(3, 5)