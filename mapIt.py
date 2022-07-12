# Goal: set up mapIt.py such that when run from the command line, the 
# script uses the command line arguments, and if there are no command
# line arguments then it will use the contents of the clipboard.

# Import webbrowser for launching the browser.
# Import sys for reading command line arguments.

import webbrowser, sys, pyperclip

# sys.argv stores a list of the program's filename and command line
# arguments. Therefore if len(sys.argv) > 1, it means that command line
# arguments have been provided. 
# ' '.join() joins each element in the string, with a space in between each
# sys.argv[1:] means starting from the 2nd element, so filename excluded

if len(sys.argv) > 1: 
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste();

# I had to run pip install pyperclip as well as sudo apt-get install xclip
# as pyperclip is not part of the Python Standard Library nor does my Linux
# virtual machine seem to have a clipboard function.

webbrowser.open('https://www.google.com/maps/place/' + address)

# Tada! Now you can copy a street name to clipboard, run this file and a 
# Google Maps browser page will open pointing at the specified street.


