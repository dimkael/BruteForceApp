
def simple_logic(login_generator, password_generator, query):
    login = login_generator.generate()
    if login is None:
        return

    while True:
        password = password_generator.generate()
        if password is None:
            return

        if query(login, password):
            print('SUCCESS', {login, password})
            return


def accounts_logic(login_generator, password_generator, query, login_limit=1000, password_limit=1000):
    success_accounts = dict()

    for _ in range(password_limit):
        password = password_generator.generate()
        if password is None:
            return

        login_generator.reset()
        for _ in range(login_limit):
            login = login_generator.generate()
            if login is None:
                break

            if login not in success_accounts.keys() and query(login, password):
                success_accounts['login'] = password
                print('SUCCESS:', (login, password))
