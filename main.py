import re
import time

from AutoEmail import Email

# Define a function for validating an Email
def check(email):
    
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return True
    else:
        return ("{} is not a valid email address".format(email))


# Driver Code
if __name__ == '__main__':

    import os
    import pandas as pd
    
    start_time = time.time()
    
    df = pd.read_excel("Donor_Address-1.xlsx").dropna()
    dL = df.values.tolist()
    listoflists = [address[0].strip() for address in dL]
    final_list = list(set(listoflists))
    
    print("Total colleted emails: {} ".format(len(final_list)))
    
    checked_list = [email for email in final_list if check(email) == True]
    
    print(checked_list)
    
    print("Total avialiable emails: {}".format(len(checked_list)))    
    
    Sender_ADDRESS = "helping.sagorika.jaist@gmail.com" # Address
    Sender_PASSWORD = "" # Password
    
    My_JAIST = Email(Sender_ADDRESS, Sender_PASSWORD)
    
    for receiver in checked_list:

        My_JAIST.send(receiver) 
    

    
    
    end_time = time.time()

    print("pass_time: {}s".format(end_time - start_time))