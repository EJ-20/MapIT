# This program launches a map in the browser using
# an address from the command line or clipboard.

# Author: Erfan Jafar
# Credits: Automate the boring stuff with Python, Al Sweigart


import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #Get address from command line
    address = "+".join(sys.argv[1:])

else: 
    # Get address from clipboard
    address = pyperclip.paste()
    address = "+".join(address.split())

webbrowser.open("www.google.com/maps/place/" + address)

