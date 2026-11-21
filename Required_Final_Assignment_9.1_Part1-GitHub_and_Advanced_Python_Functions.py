#!/usr/bin/env python
# coding: utf-8

# # Required Final Assignment 9.1 (Part 1): GitHub and Advanced Python Functions
# ---
# In this module, you learned about some more advanced Python concepts such as Python classes, functions with a variable number of positional arguments, decorators, and wrappers. In the final assignment for this module, you will be tested on your knowledge about these topics. Part 2 of the final assignment will require you to download your assignment submission from Codio and upload it to your GitHub repository.
# 
# This final coding assignment has been designed to be a comprehensive assessment of the topics covered in Module 9. The questions in the assignment are designed to be more difficult than the ones presented to you throughout the module. However, enough detail will be provided to you so that you can successfully complete the assessment.
# 
# **Remember to run your code from each cell before submitting your activity.** Running your code beforehand will notify  you of errors and  give you a chance to fix your errors 
# before submitting. 
# 
# 
# ## Index:
# 
# - [Question 1](#Question-1)
# - [Question 2](#Question-2)
# - [Question 3](#Question-3)
# - [Question 4](#Question-4)
# - [Question 5](#Question-5)
# - [Question 6](#Question-6)
# - [Question 7](#Question-7)
# - [Question 8](#Question-8)
# - [Question 9](#Question-9)
# - [Question 10](#Question-10)
# - [Question 11](#Question-11)
# - [Question 12](#Question-12)
# - [Question 13](#Question-13)

# # Python Classes
# 
# ## Question 1
# 
# *5 points*
# 
# Write a Python *class*, *`Student`*, with no attributes assigned to it.
# 
# 
# Assign the type of *`Student`* to *`ans1a`*. Assign the *`__module__`* attribute of the *`Student`* *class* to *`ans1b`*.
# 
# **HINT:** Because *`Student`* does not have any attributes, you can end its definition with the keyword *`pass.`*

# In[1]:


ans1a = None
ans1b = None

class Student:
    pass

# YOUR CODE HERE
ans1a = type(Student)
print (ans1a)

ans1b = Student.__module__
print (ans1b)


# In[ ]:





# ## Question 2
# 
# *5 points*
# 
# Modify the Python *class*, *`Student`* so that it has two attributes, *`student_name`* and *`grade`*, with values `John Smith` and `86`, respectively.
# 
# Assign the member *`student_name`* of the *class `Student`* to *`ans2a`*.

# In[2]:


### GRADED

### YOUR SOLUTION HERE
ans2a = None

class Student():
    student_name =  'John Smith' 
    grade = 86
    
# YOUR CODE HERE
ans2a = Student.student_name
print (ans2a)


# In[ ]:





# ## Question 3
# 
# *7 points*
# 
# The Python *function [`setattr`](https://docs.python.org/3/library/functions.html#setattr)* can be used to modify the attributes of a class. It basic syntax reads as follow:
# 
# ```Python
# setattr = (class_name, attribute_name, updated_value)
# 
# ```
# 
# Use the *function `setattr`* to modify the Python *class*, *`Student`* so that  *`student_name`* and *`grade`* are equal to `Angela Brooks` and `87`, respectively. Assign these operations to *`ans3a`* and *`ans3b`*, respectively.

# In[3]:


class Student:
    student_name = 'John Smith'
    mark = 86

ans3a = setattr(Student, 'student_name', 'Angela Brooks')
ans3b = setattr(Student, 'grade', 87)


# In[ ]:





# ## Question 4
# 
# *6 points*
# 
# Use a constructor to define a Python *class*, *`Student`*, with attributes *`student_name`*, *`student_id`*, *`grade`*, and *`email`*.
# 
# Construct a student, *`ans4`*, with name equal to `Francis Green`, student ID equal to `475895`, grade equal to `56`, and email address equal to `francisgreen@mit.edu`.
# 

# In[4]:


ans4 = None


# YOUR CODE HERE
class Student:
    def __init__ (self, student_name, student_id, grade, email):
        self.student_name = student_name
        self.student_id= student_id
        self.grade = grade
        self.email= email
    
ans4 = Student('Francis Green', 475895, 56, 'francisgreen@mit.edu')
print(ans4)


# In[ ]:





# ## Question 5
# 
# *7 points*
# 
# Add a *function, `curved_average`*, to the *`Student` class* defined above that takes the value stored in *`grade`* and multiplies it by `1.2`. This *function* should return a value *`updated_grade`*.
# 
# Compute the updated average of the student *`ans4`* computed in the previous questions and assign the result to *`ans5`*.

# In[5]:


ans5 = None

# YOUR CODE HERE
class Student:
    def __init__ (self, student_name, student_id, grade, email):
        self.student_name = student_name
        self.student_id= student_id
        self.grade = grade
        self.email= email
        
    def curved_average(self):
        updated_grade = self.grade*1.2
        return updated_grade
    
ans4 = Student('Francis Green', 475895, 56, 'francisgreen@mit.edu')
ans5 = ans4.curved_average()
print(ans5) 


# In[ ]:





# # Advanced Functions
# 
# ## Question 6
# 
# *7 points*
# 
# Define a *function, `my_sum`*, that computes the sum of a variable number of elements.
# 
# Assign the result of the sum of the elements `1,3,5,6`, and `10` to *`ans6a`*.
# Assign the result of the sum of the elements `10,4,6`, and `2` to *`ans6b`*.
# 

# In[6]:


### GRADED

### YOUR SOLUTION HERE
ans6a = None
ans6b = None

# YOUR CODE HERE
def my_sum(*args):
    result = 0
    for x in args:
        result =result + x
    return result

args = (1,3,5,6,10)
ans6a = my_sum(*args)
print(ans6a)

args = (10,4,6,2)
ans6b = my_sum(*args)
print(ans6b)


# In[ ]:





# ## Question 7
# 
# *8 points*
# 
# Define a *function, `my_average`*, that computes the average of a variable number of elements.
# 
# Assign the result of the sum of the elements `78,82,91,66` to *`ans7a`*.
# Assign the result of the sum of the elements `56, 89,76`, and `100` to *`ans6b`*.

# In[7]:


### GRADED

### YOUR SOLUTION HERE
ans7a = None
ans7b = None

# YOUR CODE HERE
def my_average(*args):
    suma = 0
    cn = len(args)
    for x in args:
        suma =suma + x
    avg = suma/cn
    return avg

args = (78,82,91,66)
ans7a = my_average(*args)
print(ans7a)

args = (56, 89,76,100)
ans7b = my_average(*args)
print(ans7b)


# In[ ]:





# ## Question 8
# 
# *7 points*
# 
# Suppose an invidual, say *`person1`*, has `Name` equal to `Rosie`, `Age` equal to `33`, and `Profession` equal to `Data Scientist`.
# 
# Next, suppose that another person, say `person2`*, has `Name` equal to `Kyle`, `Age` equal to `28`, and `Profession` equal to `Data Engineer`. and phone number equal to `4659874982`.
# 
# Finally, define a *function, `print_last_info()`*, that unpacks the given entries and returns the *string* in the format:
# 
# ```Python
# <key_n> is <value_n>.
# ```
# Note that in the pseudocode above, `n` represents the index for the last elements of the arguments passed to the function.
# 
# 
# Call the function with *`person1`*, and *`person2`* and assign the results to *`ans8a`* and *`ans8b`*, respectively.

# In[8]:


def print_last_info(**kwargs):
    for key, value in kwargs.items():
        string = ("{} is {}".format(key,value))
    return string

ans8a = print_last_info(Name= "Rosie", Age= 33, Profession= "Data Scientist")
ans8b = print_last_info(Name= "Kyle", Age= 28, Profession= "Data Engineer", Phone_Number=4659874982)




# In[ ]:





# ## Question 9
# 
# *7 points*
# 
# Define a *dictionary, `movie`*, with *keys* `Title`, `Director`, and `Year` and corresponding *values* `Inception`, `Nolan`, and `2010`.
# 
# 
# Define a *function, `print_movie()`*, that unpacks the entries of a provided dictionary and returns the *string* in the format:
# 
# ```Python
# <title_name_key>: <title_name_value>
# ```
# 
# 
# Call the function with the *dictionary `movie`* and assign the result to *`ans9a`*.
# 
# What happens if you also pass the argument `Music = "Zimmer"` after *`movie`*? Assign the resulting string to *`ans9b`*

# In[9]:


ans9a = None
ans9b = None


# YOUR CODE HERE
movie = {'Title':'Inception', 'Director':  'Nolan',  'Year':  2010}

def print_movie(**kwargs):
    key = list(kwargs.keys())[0]
    val = list(kwargs.values())[0]
    return f"{key}: {val}"

ans9a=print_movie(**movie)
ans9b = print_movie(**movie, Music = "Zimmer")

print(ans9a)
print(ans9b)


# In[ ]:





# # Decorators and Wrappers
# 
# 
# ## Question 10
# 
# *6 points*
# 
# Define a *function, `plus_one`*, that takes an integer as input. Within this *function*, define another *function, `add_one` that takes the same integer as input. This function should add `1` to the integer and return the result.
# 
# Finally, the *function, `plus_one`* should call the *function, `add_one`, and return the result.
# 
# Test your *functions* with the number `7` and assign the result to *`ans10`*.

# In[10]:


ans10 = None

# YOUR CODE HERE
def plus_one(n):
    def add_one(x):
        return x + 1
    return add_one(n)

ans10 = plus_one(7)
print(ans10)


# In[ ]:





# ## Question 11
# 
# *7 points*
# 
# Define a *function, `uppercase_decorator`*, that takes a function as an input. This function will contain a wrapper *function, `wrapper`*, that will  convert a *string* to uppercase.
# 
# Define another *function, `say_hello()`*, that takes no argument and returns the *string `hello there!`*. Pass the *function, `say_hello()`* to *`uppercase_decorator`* and assign the result to *`ans11`*.

# In[11]:


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hello():
    return 'hello there!'

ans11 = say_hello


# In[ ]:





# ## Question 12
# 
# *9 points*
# 
# Define a *function, `decorator_with_arguments`*, that takes a function as an input. This function will contain a wrapper *function, `wrapper_accepting_arguments`* that will take two *strings* as input and will print the *string*
# `My arguments are: <arg1>, <arg2>`.
# 
# This last step can be accomplished via the command:
# ```Python
# print("My arguments are: {0}, {1}".format(arg1,arg2))
# ```
# The *function, `decorator_with_arguments`* should return the *function, `wrapper_accepting_arguments`*.
# 
# Define another *function, `cities`*, that takes two arguments and print the *string*
# `Cities I love are: <arg1>, <arg2>`.
# 
# This last step can be accomplished via the command:
# ```Python
#  print("Cities I love are {0} and {1}".format(city_one, city_two))
# ```
# 
# Test your *functions* with the cities `Paris` and `New York` and assign the result to *`ans12`*.

# In[12]:


ans12 = None

# YOUR CODE HERE
def decorator_with_arguments(func):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1, arg2))
        return func(arg1, arg2)
    return wrapper_accepting_arguments

@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

ans12 = cities("Paris", "New York")


# In[ ]:





# ## Question 13
# 
# *9 points*
# 
# Define a *function, `decorator_passing_arbitrary_arguments`*, that takes a function as an input. This function will contain a wrapper *function, `wrapper_accepting_arbitrary_arguments`* that will take a variable number of arguments as input and will print the *string* `The positional arguments are (<arg1, arg2, arg3...>)`.
# 
# This last step can be accomplished via the command:
# ```Python
# print('The positional arguments are', args)
# ```
# The *function, `decorator_passing_arbitrary_arguments`* should return the *function, `wrapper_accepting_arbitrary_arguments`*.
# 
# Define another *function, `function_with_arguments`*, that takes three arguments and returns them as a *tuple*.
# 
# Test your *functions* with the arguments `1`, `2` and `3` and assign the result to *`ans13`*.

# In[13]:


def decorator_passing_arbitrary_arguments(function_to_decorate):
    def wrapper_accepting_arbitrary_arguments(*args):
        print('The positional arguments are', args)
        function_to_decorate(*args)
    return wrapper_accepting_arbitrary_arguments

@decorator_passing_arbitrary_arguments
def function_with_arguments_(a, b, c):
    return a, b, c

ans13 = function_with_arguments_(1,2,3) 


# In[ ]:




