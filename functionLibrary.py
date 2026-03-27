def usernameChecker():
    logged_in = False
    print("Welcome to Blockbuster!")
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
                return logged_in
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
    def __init__(self, media_type, author, name):
        if not author:
            raise ValueError ("please add an author next time")
        if media_type not in ["book", "dvd", "cd"]:
            raise ValueError ("please include an accepted media type(DVD, CD, Book)")
        self.media_type = media_type
        self.author = author
        self.name = name