#!/usr/bin/env python
# coding: utf-8

# # Python: An Overview

# ## Arithmetic Operators

# In[ ]:


# Python can execute arithmetic. 


# In[11]:


34 + 57 * 3


# In[12]:


24 / 4


# In[15]:


77 / 10


# In[7]:


77 //  10 # the quotient


# In[6]:


77 % 7 # the modulus


# In[8]:


2 ** 8 # the exponent


# In[18]:


10/3 # note simple division is slightly innacurate. Use quotient for complete accuracy


# ## Variables

# In[9]:


# It is important to distinguish the different types of variables: str, int, float, bool etc.
# Best practise is to use camel script or underscores - avoid keywords, and numbers as first character


# In[14]:


age = 20 # = is the assignment operator
age2 = 31 # this is assigning a value
age + age2 # only the most recently executed assignment is stored in memory


# In[15]:


print (age,age2) # a function used to write to the screen


# ## Casting

# In[16]:


a=35
type(a)


# In[17]:


print('fred'+str(a)) # changes type of variable to allow printing for example


# In[18]:


# Example: test score calculator


# In[25]:


student = 70
maximum = 120
percent = (student / maximum) * 100
print(round(percent,2),'%') # comma within print function acts as a space


# ## User Input

# In[2]:


userInput = input


# In[ ]:


# Exercise 5.0


# In[22]:


userName = input("Your name is: ")
userAge = int(input("You are how old? ")) # Note input is a string unless we state otherwise
print('Hello',userName,'you are',userAge,'years old. In 12 years you will be',(userAge+12),'years old')


# In[18]:


# Example: year calculator


# In[34]:


year = int(input("What year is it? "))
print('72 years ago it was the year',(Year-72))


# In[26]:


# Example: build a bill splitter


# In[24]:


print('Welcome to the Meal Price Splitter')
seats = int(input('How many people were part of the table? '))
cost = float(input('How much did the bill come to in pounds? '))
costInd = cost / seats
print('Each person should pay £',costInd,'each.')


# In[ ]:


# Example: age calculator


# In[30]:


age = input("How old are you in years? ")
months = int(age)*12
days = int(age)*365
print("You are approx",months,"months old.")
print("You are approx",days,"days old.")

