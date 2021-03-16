import requests
from pass_gens import bad_pass_gen



login = 'admin'
success = False
while not success:
    password = next(bad_pass_gen)
    data = {'login': login, 'password': password}

    response = requests.get('http://google.com/')