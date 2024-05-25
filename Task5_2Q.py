# (2Q) Write a python code using lambda function to check every element of a list is an integer or string:


newlist = [1, 'hello', 2, 'coder', 9, 'expert']

integerstring = lambda list1: all(isinstance(i, (int, str)) for i in list1)

result = integerstring(newlist)

if result == True:
    print("list contains integer and string")

else:
    print("list contains no integer and string")

# Output-> list contains integer and string

# Definition: (all )method is used to find True or False
#            (isinstance) method is used to  find Integer,string,float
#        isinstance(variable,(integer,string,float))
