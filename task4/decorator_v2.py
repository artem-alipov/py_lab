def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        if admin:
            return func(*args, **kwargs)
        else:
            return "Access denied."
    return wrapper_decorator

def get_balance():
    return 2

login = input("Login: ")
admin = False
if login == "admin":
    admin = True

get_balance = decorator(get_balance)

print(get_balance())