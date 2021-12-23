import re


# Define a function for validating an Email

def check(email):
    
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False


# Driver Code
if __name__ == '__main__':

    # Enter the email
    email = "ankitrai326@gmail.com"

    # calling run function
    print(check(email))

    email = "my.ownsite@our-earth.org"
    check(email)
    
    
    email = "my.ownsite@jaist.ac.jp"
    check(email)
    
    email = "ankitrai326.com"
    check(email)