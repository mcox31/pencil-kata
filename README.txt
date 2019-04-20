-----------------------
- PENCIL KATA         -
- AUTHOR: MICHAEL COX -
-----------------------

~Written using Test Driven Development~

------SUMMARY------
This program uses a driver program and a pencil class to emulate a crude
representation of a graphite pencil with eraser. The pencil tip and eraser 
both have durability values which degrade with use. You can write on a paper,
erase words, then write new words where those ones were before.

------INSTALLING PYTHON 3------
This program is coded in Python 3. You will need python 3 installed on your 
machine to run the program. If you do not have python 3, please install the
latest version here: https://www.python.org/downloads/ Once it's installed,
check to see if it's working by opening your terminal(MAC/LINUX) or command 
prompt(PC) and type 'python' without the quotes. You should see which version
is running and the interpreter. Type 'exit()' and hit enter to get out of the 
interpreter.

------DOWNLOADING THE REPOSITORY------
You can clone the repository into a folder by opening a git bash, navigating 
to the folder you want to use and typing 
'git clone https://github.com/mcox31/pencil-kata.git' or you can download the 
repository directly off the github site.

------RUNNING THE PROGRAMS------
navigate into the pencil-kata master folder that you downloaded using the cd 
command. Using the ls(MAC/LINUX) or dir(PC) command, you should see 5 files: 
"pencil.py", "pencilDriver.py", "pencilTests.py", "pencilDriverFunctions.py", 
and this "README.txt"

To execute the program, type 'python pencilDriver.py' and follow the on-screen 
guide.

To execute just the unit tests, type 'python pencilTests.py'

------VALUE EXPLANATIONS------
tip durability - Reduces as you write. Capital characters reduce durability by 
2. Lowercase characters reduces durability by 1. Spaces do not affect 
durability.

length - How many times the pencil can be sharpened. Sharpening resets tip 
durability. If the length reaches 0, the pencil cannot be sharpened anymore.

eraser durability - Reduces as you erase. Characters reduce eraser 
durability by one. Spaces do not affect durability.

------ERROR HANDLING------
The pencilDriver program has very rudimentary error handling. It expects 
certain inputs that should be self-explanatory. The only message you will get
is "incorrect input: please try again." Refer to expected input section for 
info.

------EXPECTED INPUT------
The first selection screen requires an integer from 1-9 (inclusive) followed by
the enter key.

Create a pencil - expects an integer value for durability, then an integer value
for length, then an integer value for eraser durability.

Edit your pencil - expects a selection by typing 1, 2, or 3 and hitting enter. 
Then expects integer values for each option.

Write with your pencil - expects a string of any length. Empty strings are 
acceptable. Does not accept escape characters.

Sharpen your pencil - no value expected.

Erase words - expects a string value which is already written. Will throw 
incorrect input error otherwise.

Write over erased words - expects an integer for an index value, it will be 0 
for the first erased word, and then one more for each erased word after that.
If you only erase one word at a time, the index value will always be 0.
Expects a new string to write after that. Same as write with your pencil.

Run unit tests - no value expected. will exit program.

Quit driver program - no value expected. will exit program.

THANK YOU FOR STOPPING BY!