import functionLibrary
# Block Buster
class Product:
    def __init__(self, name , type):
        self.name = name
        self.type = type

def main():
    logged_in = False
    print("Welcome to Blockbuster!")
    while logged_in == False:
        login_option = int(input("""""would you like to:
1 - Login
2 - create account?"""))
        if login_option == 1:
            username = input("what is your user name")
            functionLibrary.

    #loops until the exit choice is made
    while True:
        choice = int(input("""Please pick an option:
1 - borrow a product
2 - return a product
3 - recieve a recommendation
4 - make a donation
5 - exit
"""))
        if choice == 5:
            print("Thank you for visiting Blockbuster")
            break
    return
# makes sure the code doesnt run if it is called to a seperate file
if __name__ == "__main__":
    main()
