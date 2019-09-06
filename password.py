import string
from random import *
size=int(input("enter the size for password:"))
characters = string.ascii_letters + string.punctuation  + string.digits
password ="".join(choice(characters) for x in range(size))
print (password)
