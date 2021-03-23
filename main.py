import generators
import queries
import logics


# logics.get_accounts(
#     login_generator=generators.ListGenerator(tokens=['admin', 'dragon', 'samurai']),
#     password_generator=generators.BruteForceGenerator(),
#     query=queries.local_server,
#     password_limit=1000000
# )

# logics.get_logins(
#     login_generator=generators.ListGenerator(tokens=['admin', 'dragon', 'samurai']),
#     password_generator=generators.ListFileGenerator(filename='pop_passwords.txt'),
#     query=queries.local_server
# )

# logics.get_accounts(
#     login_generator=generators.ListFileGenerator(filename='pop_passwords.txt'),
#     password_generator=generators.ListFileGenerator(filename='pop_passwords.txt'),
#     query=queries.local_server
# )

logics.get_passwords(
    login_generator=generators.ListGenerator(tokens=['admin', 'dragon', 'samurai']),
    password_generator=generators.ListFileGenerator(filename='pop_passwords.txt'),
    query=queries.local_server,
    password_limit=10000
)
