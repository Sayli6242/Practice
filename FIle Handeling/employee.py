
# add employee data

def add_employee_data(file_name, name, value):

    # Open the file in append mode
    with open(file_name, "a") as file:
 
        # Write the key-value pair to the file
        file.write(f"{name}:{value}\n")


add_employee_data("sample.txt", "jenny", "25")
add_employee_data("sample.txt", "lisa", "30")


   
