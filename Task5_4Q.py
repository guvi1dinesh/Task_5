#(4Q) Write a python function to validate the regular expression for the following:
#(a) Email address
#(b) Mobile numbers of bangladesh
#(c) Telephone numbers of USA
#(d) 16 character Alpha-numeric password composed of alphabets of Uppercase,Lowercase,Special characters,Numbers


#(a) Email address:

import re
def validateemail(email):
    regex = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    pattern = re.compile(regex)

    if re.match(pattern,email):
        return True
    else:
        return False


test = "Clash@gmail.com"
output = validateemail(test)
print(output)


#Output- True


#(b) Mobile no of bangladesh:

import re
def validatemobileno(mobileno):
    regex = r'^[+880]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]'

    pattern = re.compile(regex)

    if re.match(pattern,mobileno):
        return True
    else:
        return False


test = "+8809856934289"
output = validatemobileno(test)
print(output)


#(C) USA Telephoneno:
import re


def USAtelephoneno(telephoneno):
    regex = r'^[+1]+[0-9]+[0-9]+[0-9.-]+[0-9]+[0-9]+[0-9.-]+[0-9]+[0-9]+[0-9]+[0-9]'

    pattern = re.compile(regex)

    if re.match(pattern, telephoneno):
        return True
    else:
        return False


test = '+1985-693-42898'
output = USAtelephoneno(test)
print(output)


#(D) Password Validation:
import re


def passwordvalidation(password):
    regex = r'^[a-zA-Z0-15._@*^]'

    pattern = re.compile(regex)

    if re.match(pattern, password):
        return True
    else:
        return False


test = 'Dhoni_12389@0007'
output = passwordvalidation(test)
print(output)
