# import
import random
import string

# greetings
print('Hi, Welcome to Password Generator')

# ask
length = int(input('\nPlease insert how many characters you want: '))

# defining data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combining all data
all = lower + upper + num + symbols

# random
temp = random.sample(all,length)

# make password
password = "".join(temp)

# tell the password
print(password)