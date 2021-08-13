import string
import random

s1 = string.ascii_lowercase  # all the characters in lowercase
s2 = string.ascii_uppercase  # all the characters in uppercase
s3 = string.digits  # all the digits
s4 = string.punctuation  # all the punctuation

len = int(input("Enter the length of password \n"))  # Max length of password

s = []  # creating an empty list
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)  # all the characters in one list

print('Your password is \n')

print("".join(random.sample(s, len)))  # using random.sample(sequence,length)
                                       # using join we are concatenating the random characters
