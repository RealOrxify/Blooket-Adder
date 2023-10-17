import colorama
from colorama import Fore, Style

colorama.init()

def blooket_token_adder(username, tokens):
    print(Fore.BLUE + Style.BRIGHT + "Adding " + str(tokens) + " tokens to " + username + "...")
    # Add token adding logic here

if __name__ == "__main__":
    username = input("Enter your blooket username: ")
    tokens = int(input("Enter the number of tokens to add: "))
    blooket_token_adder(username, tokens)
