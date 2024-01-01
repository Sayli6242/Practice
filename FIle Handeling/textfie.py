# import os
# import subprocess

# # user_input = str(input("enter command: "))
# # result = os.system(user_input)

# # print(result.stdout)
# # import subprocess

# # cmd = "date"

# # # returns output as byte string
# # returned_output = subprocess.check_output(cmd)

# # # using decode() function to convert byte string to string
# # print('Current date is:', returned_output.decode("utf-8"))

# import subprocess
# import os

# # Run commands in a loop until the user decides to exit
# while True:
#     # Get the current working directory
#     current_directory = os.getcwd()

#     # Prompt the user to enter a command
#     user_input = input(f"Current directory: {current_directory}\nEnter a Linux command (or 'exit' to quit): ").strip()

#     # Check if the user wants to exit the loop
#     if user_input.lower() == 'exit':
#         break

#     try:
#         # Run the user's command and capture the output
#         result = subprocess.run(user_input, shell=True, capture_output=True, text=True)

#         # Print the command's output
#         print("\nCommand output:")
#         print(result.stdout)

#         # Print any error messages if the command failed
#         if result.returncode != 0:
#             print("\nCommand error:")
#             print(result.stderr)

#     except Exception as e:
#         print(f"An error occurred: {e}")

# print("Program ended.")
import subprocess


def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


if __name__ == '__main__':
    hello_command = "ls"
    hello_info = run(hello_command)
    print(hello_info.stdout)
    if hello_info.returncode != 0:
        print("An error occured: %s", hello_info.stderr)
    else:
        print("Hello command executed successfully!")
    
    print("-------------------------")
    
   




















