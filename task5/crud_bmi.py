import os

users = {}
user_counter = 0

def user_info():
    user_id = input("Enter user ID: ")
    if user_id in users:
        user = users[user_id]
        print(f"User ID: {user_id}")
        print(f"Login: {user['login']}")
        print(f"Height: {user['height']}")
        print(f"Age: {user['age']}")
        print(f"Gender: {user['gender']}")
        print(f"Weight: {user['weight']}")
        bmi = user['weight'] / (user['height'] / 100) ** 2
        bmi_min, bmi_max = 16, 50
        bmi_scale = ''.join(['=','|'][i==round((bmi-bmi_min)*33/(bmi_max-bmi_min))] for i in range(34))
        print("Your BMI is {:.2f}".format(bmi))
        print("BMI: 16 {} 50".format(bmi_scale, bmi_min, bmi_max))
    else:
        print("User not found.")

def update_user():
    user_id = input("Enter user ID: ")
    if user_id in users:
        user = users[user_id]
        print(f"Current user info: {user}")
        user['height'] = float(input("Enter new height: "))
        user['age'] = int(input("Enter new age: "))
        user['gender'] = input("Enter new gender: ")
        user['weight'] = float(input("Enter new weight: "))
        users[user_id] = user
        print("User info updated.")
    else:
        print("User not found.")

def delete_user():
    user_id = input("Enter user ID: ")
    if user_id in users:
        del users[user_id]
        print("User deleted.")
    else:
        print("User not found.")

def add_user():
    global user_counter
    login = input("Enter user login: ")
    height = float(input("Enter height (in cm): "))
    age = int(input("Enter age: "))
    gender = input("Enter gender (M/F): ")
    weight = float(input("Enter weight (in kg): "))
    user_counter += 1
    user_id = f"U{user_counter}"
    user = {'login': login, 'height': round(height), 'age': age, 'gender': gender, 'weight': round(weight)}
    users[user_id] = user
    print("User added. User ID:", user_id)

def process_option(option):
    if option == '1':
        print("==== User List ====")
        for user_id, user in users.items():
            print(user_id, user['login'])
        print("===================")
    elif option == '2':
        return user_info()
    elif option == '3':
        return update_user()
    elif option == '4':
        add_user()        
    elif option == '5':
        return delete_user()
    
def print_menu():
    print('''==== BMI Calculator Menu ====
    1. Show User List
    2. Show User Info
    3. Change User Info
    4. Add New User
    5. Delete User
    6. Exit Program''')

def main():
    os.system('CLS')
    print_menu()
    option = input('Choose option: ')
    while option != "6":
        os.system('CLS')
        process_option(option)
        input("Please press Enter to continue...")
        os.system('CLS')
        print_menu()
        option = input('Choose option: ')
    print("Good bye") 

main()