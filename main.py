from models import user_crud


db_path = "db_handler/users.json"

def init():
    print("\n**********WELCOME TO TECH MINDS**********\n")
    print("Enter 1 to register for participation")
    print("Enter 2 to exit")

    responses = input("Choose an option")

    if responses == "1":
        register()
    elif responses == "2":
        print("Thanks for trying to register")
    else:
        print("\nInvalid response \nTry again")
        init()

"""
creating a registration class
"""
def register():
    print("\nProvide the following details to create an account")
    name = input("Enter your full name\n")
    email = input("Enter your email\n")
    
    if name == "" or email == "":
        print("\nThese fields cannot be blank")
    else:
        user_details = {
            "name":name,
            "email":email,
        }
        response = user_crud.create_user(db_path,user_details)
        if response == 1:
            print("\nUser creation success")
            print("Redirected home")
            init()
        else:
            print("\nUser with such email account already exist")
            print("Enter 1 to retry \nEnter anything to go home", init, register)

init()