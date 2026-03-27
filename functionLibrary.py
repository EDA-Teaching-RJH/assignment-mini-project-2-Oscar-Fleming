import random
def usernameChecker():
    logged_in = False
    print("Welcome to the music store!")
    while logged_in == False:
        login_option = int(input("""would you like to:
1 - Login?
2 - create account?
"""))
        if login_option == 1:
            usernames = []
            username = input("What's your username ")
            logged_in = False
            with open("logins.txt", "r") as file:
                usernames = file.readlines()
                usernames = [x.rstrip("\n") for x in usernames]# to remove the new line that forms in the text file
            for i in range(len(usernames)):
                if usernames[i] == username:
                    logged_in = True
            if logged_in == True:
                print(username, " - successfully logged in")
                return username , logged_in
            else: 
                print("invalid username")
        if login_option == 2: 
            usernames = []
            logged_in = False
            new_login = input("please choose a username ")
            #reusing login formula to check for reused usernames
            username = new_login
            with open("logins.txt", "r") as file:
                usernames = file.readlines()
                usernames = [x.rstrip("\n") for x in usernames]
            for i in range(len(usernames)):
                if usernames[i] == username:
                    logged_in = True
            if logged_in == True:
                print("username already in use, please pick another")
                logged_in = False # to make sure it doesnt break the while loop
            else:
                new_login = "\n" + str(new_login) # \n to make sure each entry gets its own line in the txt file and therefore its own position in the list
                with open ("logins.txt", "a") as file:
                    file.write (new_login)
                print("new username successfully added to database ")

class Content:
    def __init__(self, artist, name):
        if not name:
            raise ValueError ("please add a name next time")
        if not artist:
            raise ValueError ("please add an artist next time")
        self.artist = artist
        self.name = name
def info_collector():
    cd_name = input("please name the cd ").lower()
    artist = input("please name the artist of the cd ").lower()
    return cd_name, artist
def borrow():
    cd_name = input("what is the name of the cd you are looking to borrow ")
    with open ("CDs.txt", "r")as file:
        cds = file.readlines()
        file.close
    cds = [x.rstrip("\n") for x in cds]
    with open ("borrowed?.txt", "r") as file:
        borrow_status = file.readlines()
        borrow_status = [x.rstrip("\n") for x in borrow_status]
        for i in range(len(cds)):
            if cds[i] == cd_name:
                if borrow_status[i] == "borrowed":
                    print("CD is currently borrowed")
                else:
                    borrow_status[i] = "borrowed"
                    print("CD found and in stock!")
                    print("you have borrowed", cd_name)
        for i in range(len(cds)-1):# lines 74-80 delete the currently saved list of what is 
            borrow_status[i] = (borrow_status[i] + "\n")#borrowed or not and replaces it with the updated list stored in the program
        with open ("borrowed?.txt", "w")as file:
            file.close
        for i in range(len(cds)):
            with open("borrowed?.txt", "a") as file:
                file.write(borrow_status[i])
def returns():
    cd = input("which CD would you like to return")
    with open ("CDs.txt", "r")as file:
        cds = file.readlines()
    cds = [x.rstrip("\n") for x in cds]
    with open ("borrowed?.txt", "r") as file:
        borrow_status = file.readlines()
        borrow_status = [x.rstrip("\n") for x in borrow_status]
        for i in range(len(cds)):
            if cds[i] == cd:
                if borrow_status[i] == "borrowed":
                    print("book will now be returned")
                    borrow_status[i] = ""
                else:
                    print("cd is not lent out currently")
        for i in range(len(cds)-1):
            borrow_status[i] = (borrow_status[i] + "\n")
        with open ("borrowed?.txt", "w")as file:
            file.close
        for i in range(len(cds)):
            with open("borrowed?.txt", "a") as file:
                file.write(borrow_status[i])
def recommendation():




def donation():
    name, cd_artist = info_collector()
    with open("CDs.txt", "a") as file:
        file.write("\n" + str(name))
    with open("authors.txt", "a") as file:
        file.write("\n" + str(cd_artist))
    with open ("borrowed?.txt", "a") as file:
        file.write("\n")
    