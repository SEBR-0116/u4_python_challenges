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
# Function to convert minutes to seconds
def minutes_to_seconds(minutes):
    return minutes * 60
minutes = 5
seconds = minutes_to_seconds(minutes)

# Function to convert hours to seconds
def hours_to_seconds(hours):
    return hours * 3600
hours = 2
seconds = hours_to_seconds(hours)

# Calculate the total seconds in a day
def calculate_seconds_in_a_day():
    hours_per_day = 24
    return hours_to_seconds(hours_per_day)
seconds_in_a_day = calculate_seconds_in_a_day()

# Calculate the total hours in the month of June
def calculate_hours_in_june():
    days_in_june = 30
    hours_per_day = 24
    return days_in_june * hours_per_day

# Calculate the total minutes in the month of August
def calculate_minutes_in_august():
    days_in_august = 31
    hours_per_day = 24
    minutes_per_hour = 60
    return days_in_august * hours_per_day * minutes_per_hour

# Perform the calculations
seconds_in_a_day = calculate_seconds_in_a_day()
hours_in_june = calculate_hours_in_june()
minutes_in_august = calculate_minutes_in_august()

# Print results
print(f"{minutes} minutes is equal to {seconds} seconds.")
print(f"{hours} hours is equal to {seconds} seconds.")
print(f"There are {seconds_in_a_day} seconds in a day.")
print(f"Seconds in a day: {seconds_in_a_day}")
print(f"Hours in June: {hours_in_june}")
print(f"Minutes in August: {minutes_in_august}")

# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
def mid(string):
    length = len(string)
    if length % 2 == 0:
        return ""
    else:
        middle_index = length // 2
        return string[middle_index]

print(mid("Hello"))  # Output: "l"
print(mid("Python")) # Output: "t"
print(mid("AI"))     # Output: ""


# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
def hide_credit_card_number(card_number):
    if len(card_number) < 4:
        return "Invalid card number"  # Return error message if the length is less than 4
    
    hidden_digits = '*' * (len(card_number) - 4)  # Hide all characters except the last four
    visible_digits = card_number[-4:]  # Extract the last four characters
    
    return hidden_digits + visible_digits

# Example usage:
print(hide_credit_card_number("1234567894444"))  # Output: "*********4444"
print(hide_credit_card_number("1234"))           # Output: "1234" (length less than 4)
print(hide_credit_card_number("123"))            # Output: "Invalid card number" (length less than 4)

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
def online_count(statuses):
    count = 0
    for status in statuses.values():
        if status == "online":
            count += 1
    return count

statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

print(online_count(statuses))  # Output: 2

# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
def apply_discount(full_price, discount_percentage):
    discounted_amount = (discount_percentage / 100) * full_price
    discounted_price = full_price - discounted_amount
    return discounted_price

# Example usage:
full_price = 100
discount_percentage = 20
discounted_price = apply_discount(full_price, discount_percentage)
print(discounted_price)  # Output: 80

# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
def calculate_hypotenuse(adjacent, opposite):
    hypotenuse = (adjacent ** 2 + opposite ** 2) ** 0.5
    return int(hypotenuse)

adjacent_leg = 3
opposite_leg = 4
hypotenuse = calculate_hypotenuse(adjacent_leg, opposite_leg)
print(hypotenuse)  # Output: 5

# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------

# ---------------------------------
