# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


def time_stone(x):
    #return x*60 # minutes
    #return x*3600 # hours
    #return x*3600*24 # day
    #return x*3600*24*30 # 30-day month (June)
    #return x*3600*24*31 # 31-day month (August)
    return x*3600*24*365 # year
print(time_stone(1))



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


def mid(string):
    if len(string) % 2 == 0:
        return""
    else:
        return string[len(string)//2]


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


def credit_id(num):
    last_4=num[-4:]
    hide_num = len(num[:-4])
    num = num.replace(num[:-4], "*" * hide_num)
    print(num)
credit_id('1234567890')



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

#   Got help from https://www.geeksforgeeks.org/python-count-keys-with-particular-value-in-dictionary/
statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}
is_online = "online"
res = 0
for key in statuses:
    if statuses[key] == is_online:
        res = res + 1
print('People Online: ' + str(res))
# -> seems like an outdated print method but I couldn't figure out a cleaner way using this method



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

def sale_total(full_price, discount):
    return full_price - discount
print(sale_total(100, 20))


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


def pythag_hypotenuse(opposite, adjacent):
    import math
    return math.sqrt(opposite**2 + adjacent**2)
print(pythag_hypotenuse(10, 20))


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# this is how I think you'd do it where you can pick two numbers to evaluate like the prompt says, so they wouldn't have to be part of the actual sequence to follow the same pattern
#   -> also, this gets the intervals instead of the sums
#   -> kind of cumbersome but I wasn't sure how to do like n-1 math when you needed to be able to input two variables
def fibonacci(a, b):
    c = a + b #3 0 + 1 = 1 (Interval: 1)
    d = b + c #4 1 + 1 = 2 (Interval: 2)
    e = c + d #5 1 + 2 = 3 (Interval: 3)
    f = d + e #6 2 + 3 = 5 (Interval: 4)
    g = e + f #7 3 + 5 = 8 (Interval: 5)
    h = f + g #8 5 + 8 = 13 (Interval: 6)
    i = g + h #9 8 + 13 = 21 (Interval: 7)
    j = h + i #10 13 + 21 = 34 (Interval: 8)
    k = i + j #11 21 + 34 = 55 (Interval: 9)
    
    return (c, d, e, f, g, h, i, j, k)
print(fibonacci(0, 1))

