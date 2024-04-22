# My Second Project Random Password Generate:
import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# Create a password with letets & digits
pass_len=7
value=string.ascii_letters + string.digits

password=""

# Password Generate:
for i in range(pass_len):
  password+=random.choice(value)

print("Your Random Password is:",password)