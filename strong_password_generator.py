import random
import string as s

def pass_generator(length=10):
    characters = s.digits + s.ascii_letters + s.digits + s.punctuation
    return ''.join(random.choice(characters) for i in range(length))

print ("The Random String :", pass_generator(10))