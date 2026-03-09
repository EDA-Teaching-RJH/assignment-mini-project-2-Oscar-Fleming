import functionLibrary
# Block Buster
class Product:
    def __init__(self, name , type):
        self.name = name
        self.type = type

def main():
    while True:
        print("""Welcome to Blockbuster!
              Please pick an option:
              1 - borrow a product
              2 - return a product
              3 - recieve a recommendation
              4 - make a donation
              5 - exit""")
        break
    return
    
# makes sure the code doesnt run if it is called to a seperate file
if __name__ == "__main__":
    main()
