import random
import string


with open('pop_passwords.txt') as file:
    pop_passwords = file.read()
pop_passwords = pop_passwords.split('\n')


alphabet = string.ascii_letters + string.digits + string.punctuation
def good_pass_gen(length=10):
    return ''.join([random.choice(alphabet) for i in range(length)])


bad_pass_gen = (pop_passwords[i] for i in range(len(pop_passwords)))