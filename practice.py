# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 14:41:04 2015

@author: marriott
"""

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
print "{0} is {1} years old, {0}".format(name, age)
print '{0} is {1} years old, {0}'.format(name, age)
