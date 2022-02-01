import pyperclip as pc
import random
import string
punctuations = '!-<>?@#$%^&*_~'

def strongPassword(minimum, maximum):
    return ''.join((random.choice(string.ascii_letters + string.digits + punctuations) for x in range((maximum+1)- minimum)))

minimum, maximum = 4, 12
password = strongPassword(minimum, maximum)

pc.copy(password)
print(password)

