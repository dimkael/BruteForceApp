import string


class BruteForceGenerator:
    def __init__(self, alphabet=string.digits + string.ascii_lowercase):
        self.alphabet = alphabet
        self.base = len(self.alphabet)
        self.length = 0
        self.i = 0

    def reset(self):
        self.length = 0
        self.i = 0

    def generate(self):
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


class ListGenerator:
    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0

    def reset(self):
        self.i = 0

    def generate(self):
        if self.i >= len(self.tokens):
            return

        token = self.tokens[self.i]
        self.i += 1
        return token


class ListFileGenerator(ListGenerator):
    def __init__(self, filename='pop_passwords.txt'):
        with open(filename) as file:
            tokens = file.read().split('\n')

        super().__init__(tokens=tokens)
