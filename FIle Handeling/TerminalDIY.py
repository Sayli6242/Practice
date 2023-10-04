# to make terminal 
"""
- we have to run terminal in while loop(continuously).
- we have to take input from terminal in new line always.(\n)
- always show current directory path.
- run commands.
- we have to display output of run commands.

"""

# import operating system
import os
import subprocess

# run program in loop
while True:
    # ger current working directory
    directory = os.getcwd()
    print(directory)
    # take input in new line always
    # take_input = input("\nenter command: \n")
    subprocess.Popen('echo"geek"', shell= True)
