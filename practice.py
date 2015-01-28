# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 14:41:04 2015

@author: marriott
"""

# Help and guidence from http://www.swaroopch.com/notes/python/

print "Hello World" # this will display test in the " " in the console

print 'Single quotes can also be used'  #This preserves all white space and tabs

print   """ 
        This is a tripple quote structure
        allows multi line print statements
        and keeps them on the new line,
        also "keeps the quote marks"
        """
# A note on strings: they are immutable, once created they cannot be changed
# Single and double quotes are the same 
    
# Using the Format() method allows you to use variables in strings
age = 24
name = "Chris"        # These are both variables

# Showing that using " and ' result in same output
print "{0} is {1} years old".format(name, age)
print '{0} is {1} years old'.format(name, age)
# The {0} refers to the first argument in the format function and
# the {1} refers to the second argument

# Doing the same as above but with concatination
print name + ' is ' + str(age) + ' years old.'  
# The str() function allows the age which is a number to be interpreted as
# a string, this is uglier and more error prone

