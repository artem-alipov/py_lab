def decorator(func):
    def wrapper_decorator():
        login = input("Login: ")
        if login == "admin":
            return func()
        else:
            return "Access denied" 
    return wrapper_decorator
@decorator
def get_balance():
    return 2

print(get_balance())