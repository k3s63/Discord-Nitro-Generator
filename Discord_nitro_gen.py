#Don't copy this code 

import webbrowser
webbrowser.open("https://t.me/pythontoolgod")

import os
os.system('pip install discord_webhook')
os.system('cls' if os.name == 'nt' else 'clear')
from discord_webhook import DiscordWebhook
import requests
import random
import string
import time
import os
class NitroGen: 
    def __init__(self): 
        self.fileName = "Nitro Codes.txt" 

    def main(self): 
        os.system('cls' if os.name == 'nt' else 'clear') 

        print(""" 
          ██╗  ██╗██████╗ ███████╗ ██████╗ ██████╗ 
          ██║ ██╔╝╚════██╗██╔════╝██╔════╝ ╚════██╗
          █████╔╝  █████╔╝███████╗███████╗  █████╔╝
          ██╔═██╗  ╚═══██╗╚════██║██╔═══██╗ ╚═══██╗
          ██║  ██╗██████╔╝███████║╚██████╔╝██████╔╝
         ╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ 

                                                        """) 
        
        time.sleep(2) 
        self.slowType("Made by: @K3S63   ", .02) 
        print()
        self.slowType("This gen bot gen nitro code take a valid code and redeem it.", .02)
        self.slowType(" If You want to give feedback than Contact Me using this telegram bot @k3s63_support_bot !" , .02)
        self.slowType("Best of luck for Gen! It will take time to get a hit, but it will definitely be successful.", .02)
   
        time.sleep(2) # Wait a little more
        self.slowType("\nInput How Many Codes to Generate and Check: ", .02, newLine = False) # Print the first question

        num = int(input('')) # Ask the user for the amount of codes

        # Get the webhook url, if the user does not wish to use a webhook the message will be an empty string
        self.slowType("\nDo you want to use a discord webhook? \nIf so type it here or press enter to dont use an webhook: ", .02, newLine = False)
        url = input('') # Get the awnser
        webhook = url if url != "" else None # If the url is empty make it be None insted

        print() # Print a newline for looks

        valid = [] # Keep track of valid codes
        invalid = 0 # Keep track of how many invalid codes was detected

        for i in range(num): # Loop over the amount of codes to check
            code = "".join(random.choices( # Generate the id for the gift
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            ))
            url = f"https://discord.gift/{code}" # Generate the url

            result = self.quickChecker(url, webhook) # Check the codes

            if result: # If the code was valid
                valid.append(url) # Add that code to the list of found codes
            else: # If the code was not valid
                invalid += 1 # Increase the invalid counter by one

            if result and webhook is None: # If the code was found and the webhook is not setup
                break # End the script


        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") 

        input("\nSuccesfully Genertated Nitro Codes. Valid will codes save on your device in a txt file named as 'Nitro Codes.txt' If not got a hit than run the file again! Press Enter 5 times to close the program. Or Refresh The Page to use the gen again") # Tell the user the program finished
        [input(i) for i in range(4,0,-1)] # Wait for 4 enter presses


    def slowType(self, text, speed, newLine = True): 
        for i in text: 
            print(i, end = "", flush = True) 
            time.sleep(speed) 
        if newLine: 
            print() 

    def generator(self, amount): 
        with open(self.fileName, "w", encoding="utf-8") as file: 
            print("Wait, Generating for you") 

            start = time.time() 

            for i in range(amount): 
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) 

                file.write(f"https://discord.gift/{code}\n") 

           
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n")

    def fileChecker(self, notify = None):
        valid = [] 
        invalid = 0 
        with open(self.fileName, "r", encoding="utf-8") as file: 
            for line in file.readlines(): 
                nitro = line.strip("\n") 

                
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) 

                if response.status_code == 200: 
                    print(f" Valid | {nitro} ") 
                    valid.append(nitro)

                    if notify is not None: 
                        DiscordWebhook( # Send the message to discord letting th user know there has been a valid nitro code
                            url = notify,
                            content = f"Valid Nito Code detected! @everyone @here  \n{nitro}"
                        ).execute()
                    else: 
                        break 

                else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
                    print(f"  Not valid | {nitro} ") # Tell the user it tested a code and it was invalid
                    invalid += 1 # Increase the invalid counter by one

        return {"valid" : valid, "invaild" : invalid} # Return a report of the results

    def quickChecker(self, nitro, notify = None): # Used to check a single code at a time
        # Generate the request url
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) # Get the response from discord

        if response.status_code == 200: # If the responce went through
            print(f" Valid | {nitro} ") # Notify the user the code was valid

            if notify is not None: # If a webhook has been added
                DiscordWebhook( # Send the message to discord letting the user know there has been a valid nitro code
                    url = notify,
                    content = f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True # Tell the main function the code was found

        else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
            print(f" Invalid | {nitro} ") # Tell the user it tested a code and it was invalid
            return False # Tell the main function there was not a code found

if __name__ == '__main__':
    Gen = NitroGen() # Create the nitro generator object
    Gen.main() #by @k3s63
