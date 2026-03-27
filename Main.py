import functionLibrary
# Block Buster
class Product:
    def __init__(self, name , type):
        self.name = name
        self.type = type

def main():
    name, logged_in = functionLibrary.usernameChecker()

    #loops until the exit choice is made
    while logged_in == True:
        try:
            choice = int(input("""Please pick an option:
1 - borrow a product
2 - return a product
3 - recieve a recommendation
4 - make a donation
5 - find a product
6 - exit
"""))
            assert choice >= 1 and choice <= 6
        except  AssertionError:
            print ("please pick a valid option")
        if choice == 1:
            functionLibrary.borrow()
        elif choice == 2:
            functionLibrary.returns()
        elif choice == 3:
            functionLibrary.recommendation()
        elif choice == 4:
            functionLibrary.donation()
        elif choice == 5:
            functionLibrary.search()
        elif choice == 6:
            print("Thank you for visiting Blockbuster")
            logged_in = False
    return
# makes sure the code doesnt run if it is called to a seperate file
if __name__ == "__main__":
    main()
