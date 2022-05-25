# CS106 Lab
# September 9, 2020
# Names and roles of group members: Farah, Eric, Ryan

######################################################################
# Problem 1 (Textbook Exercise 1.5)
print('***** Problem 1:') # Do not change this line of code
# Fix the code

# Question 1a: What happens when you run this 'buggy' code?
# Answer: An Error message comes up pointing out the primt isn't a function

# Question 1b: What needs to be fixed in this 'buggy' code?
# Answer: rewrite the print statement with correct spelling and correct
# () usage

# Code to run then fix:
# This code should print the message Hello World! to the screen.
print ('Hello world!')

######################################################################
# Problem 2
print('\n\n***** Problem 2:') # Do not change this line of code
# Fix the code

# Question 2a: What happens when you run this 'buggy' code?
# Answer: It prints the letter z, not the variable z, because its in quotation marks

# Question 2b: What needs to be fixed in this 'buggy' code? Hint - you need to
# add some lines of code.
# Answer: Firstly, you have to assign x and y some type of value in this case I will assign integer values,
# secondly, after assigning integers you must print z without quotation marks

x = 10
y = 15
z = x + y
print(z)

######################################################################

# Problem 3 (Textbook Exercise 2.3)
print('\n\n***** Problem 3:') # Do not change this line of code

wage = input("What is your hourly wage ")
hours = input("How many hours do you work per week ")
pay = (float(wage) * float(hours))
print(("The pay based on your information is $") + str(pay))

######################################################################
# Problem 4 - Bonus Problem
# Work on this problem if you finish the first 3 problems before the end
# of group work time. If you do not work on this with your lab group, use this
# problem for practice and studying.
print('\n\n***** Problem 4:') # Do not change this line of code

# This code is a useful tool for when you are shopping at the grocery store.
# Often the store gives the price for a certain quantity of the item, such as
# two mangoes costs $3. However, you may want to purchase a different quantity,
# such as five mangoes, and you need to calculate how much you will pay.

# Write code to prompt the user to input the price and quantity specified by
# the store, along with the number of the item that the user wants to purchase.
# The program should output the cost that the user will pay for the number items
# she is purchasing.
#
# See the example output in the document for this lab on theSpring.
# Write your code for Problem 4 here:

amounts = input("How many mangos do you want? ")
mango_price = 3 / 2
print("The price for one mango is " + str(mango_price))
checkout = float(mango_price ) * float(amounts)
overall_cost = print("Today's cost for your mangoes will be $" + str((checkout)))
