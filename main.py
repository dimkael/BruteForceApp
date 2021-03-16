import requests
from pass_gens import bad_pass_gen


if __name__ == '__main__':
    login = 'admin'
    success = False
    while not success:
        password = next(bad_pass_gen)
        data = {'login': login, 'password': password}

        response = requests.get('http://google.com/')