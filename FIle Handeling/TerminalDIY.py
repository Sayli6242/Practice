 # to make terminal 
"""
- we have to run terminal in while loop(continuously).
- we have to take input from terminal in new line always.(\n)
- always show current directory path.
- run commands.
- we have to display output of run commands.

"""

# import operating system
import subprocess
import os
# run program in loop
while True:
    # ger current working directory
    current_directory = os.getcwd()
    print(current_directory)
 
    # take input in new line always
    user_input = input("enter command: ").strip()
        # use module to execute commands
        # result = subprocess.run(user_input, shell= True)
        # print(result.stdout)
    try:
        result = subprocess.run(user_input, shell=True, capture_output=True, text=True)
    
        print(result.stdout)

        # check command is run or failed if failed then return error
        if result == None:
            print(result.stderr)

    # use expect block to catch exception
    except Exception as e:
        print("error occured")

# print ending msg when while loop is intreputed
print("this session is ended ")