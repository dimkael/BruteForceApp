import generators
import queries
import logics


# logics.simple_logic(
#     login_generator=generators.ListGenerator(tokens=['admin', 'dragon', 'samurai']),
#     password_generator=generators.ListFileGenerator(filename='pop_passwords.txt'),
#     query=queries.local_server
# )

logics.accounts_logic(
    login_generator=generators.ListGenerator(tokens=['admin', 'dragon', 'samurai']),
    password_generator=generators.ListFileGenerator(filename='pop_passwords.txt'),
    query=queries.local_server
)
