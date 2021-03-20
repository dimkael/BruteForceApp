import string


class BruteForceGenerator:
    def __init__(self):
        self.alphabet = string.digits + string.ascii_lowercase
        self.base = len(self.alphabet)
        self.length = 0
        self.i = 0

    def reset(self):
        self.length = 0
        self.i = 0

    def brute_force(self):
        x = self.i
        result = ''

        while len(result) < self.length:
            rest = x % self.base  # остаток от деления
            x //= self.base  # целая часть от деления
            result = self.alphabet[rest] + result
            break

        if result == self.alphabet[-1] * self.length:
            self.length += 1
            self.i = 0
        else:
            self.i += 1

        return result


class PopularPasswordsGenerator():
    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits + string.punctuation
        with open('pop_passwords.txt') as file:
            self.pop_passwords = file.read()
        self.pop_passwords = self.pop_passwords.split('\n')

    def reset(self):
        self.i = 0

    def generate(self):
        password = self.pop_passwords[self.i]
        self.i += 1
        return password