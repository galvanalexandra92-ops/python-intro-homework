# What the error message said:
# TypeError: can only concatenate str (not "int") to str
#
# What caused it:
# input() always returns text (a string), even when I type a number.
# On line 2, I tried to add the number 5 to that text, and Python
# can't add a string and an integer together.
#
# How I fixed it:
# I wrapped input() in int() so age becomes a number before I add 5.
age = int(input("How old are you? "))
print(age + 5)