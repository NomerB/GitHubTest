# This is a demo program
print('Hello World!')

# Comments
# first - using hash (#) character
print('Laguna University')
#print('Laguna University')

# Second is the use of triple single or double quote '''...''' or """...""" - for multi line comment
'''
print('Laguna University')
print('Sta. Cruz, Laguna')
'''
print('Laguna University')
print('Sta. Cruz, Laguna')

# Third is the use of docstring comment is mostly used in the module, function, class or method
# We can check a function's docstring by using the __doc__ attribute.
# Generally, four whitespaces are used as the indentation.
# The amount of indentation depends on user setting, but it must be consistent throughout that block.

def intro():
   """
   This function prints Hello Joseph
   """
   print("Hello Joseph")

# Note: The docstring must be the first thing in the function; otherwise, Python interpreter cannot get the docstring.
intro.__doc__
intro()

# these are all for the moment
