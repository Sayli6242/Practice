# file based key value database

"""
1) first open file.
2) then read each line of file by applying loop. 
3) perform operations:
        - get(key): Retrieve the value associated with a key.
            - first read the file by using read mode
            - read each line using readline.
            - split key and value by using colon ":".
            - check key matches to given key.
            - return value if key found.
            - return none if not found

        - put(key, value): Insert a value into the database associated with a key.
            - open file read- write mode
            - check if existing key is present in file or not
            - if exist return error
            - if not insert key(read all lines using redline and then insert new pair on new line)
            - write key  pair

        - delete(key): Remove the value associated with a key.
            - Open the database file in reading ('r' mode)
            - read eachline of file using readline
            - check key is matched with provided key or not
            - if matched then remove line
            - if key not matched then return error

        - update(key, value): Update the value associated with a key.
            - Open database fiel in read- write mode
            - Check if the key does not match the requested key
            - if maches then remove whole line
            - Update the new line with the new value 
            - Write the updated lines back to the end of file

# """

fileptr = "key_value_database.txt"

def main():
    while True:
        print("which operation you want to perform:\n 1) get(key): Retrieve the value associated with a key.\n 2) put(key, value): Insert a value into the database associated with a key\n 3) delete(key): Remove the value associated with a key\n 4)update(key, value): Update the value associated with a key.")
        option_input = int(input('enter option: ').strip())

        if option_input == 1:
            key = input("enter key to retrieve value associated with: ")
            result = get_key(fileptr, key)
            if result is not None:
                print(f"Value for key '{key}': {result}")
            else:
                print(f"Key '{key}' not found.")


        if option_input == 2:
            key = input("enter key to add: ")
            value = input("enter value to associate key: ")
            result = put_key(fileptr, key, value)
            if result:
                print(f"Key '{key}' added successfully.")
            else:
                print(f"Key '{key}' already exists.")
        
        if option_input == 3:
            key_to_remove = input("enter key you want to delete: ")
            result = delete_key(fileptr, key_to_remove)
            if result:
                print(f"Key '{key_to_remove}' deleted successfully.")
            else:
                print(f"Key '{key_to_remove}' not found. Nothing to delete.")

        
        if option_input == 4:
            key_to_update = input("enter key whose value want to update: ")
            new_value = input("enter new value associate to key: ")
            result = update_key(fileptr, key_to_update, new_value)
            if result:
                print(f"Key '{key_to_update}' updated successfully.")
            else:
                print(f"Key '{key_to_update}' not found. Cannot update.")

            break
    
    else:
        print("invalid input. try again")

#  Retrieve the value associated with a key.
def get_key(fileptr, key):
     # Open the database file for read mode 

    with open(fileptr, 'r') as file: 
        # Read the next line from the file
        file.readline()
        for line in file: 
        
        # Split the line into key and value using ':' as the delimiter
            a = line.strip().split(':')
            k = a[0]
            v = a[1]
                # Check if the key matches the requested key
            if k == key:  
                # Return the value if the key is found
                return v
    return None

# Insert a value into the database associated with a key.
def put_key(fileptr, key, value):
    # open file in read-write mode
    with open(fileptr, 'r+') as file:
        lines = file.readlines()
        # iterate loop for each line
        for line in lines:
            parts = line.strip().split(':')

            existing_key, _ = parts
            # check if existing key is present in file or not
            if existing_key == key:
                print('error: key already existed')
                return False
            
            # write key  pair
        new_line = f"{key}:{value}\n"

        file.write(new_line)
        return True


# Remove the value associated with a key.
def delete_key(fileptr, key_to_remove):
    # Open the database file in read-write mode
    with open(fileptr, "r+") as file:
        # Read all lines from the file into a list
        lines = file.readlines()
        #list to store the updated lines
        updated_lines = [] 
        result = False

        # Iterate through each line in the file
        for line in lines:
            # Split the line into key and value using ':' as the delimiter
            parts = line.strip().split(':')
            key, _ = parts

            # Check if the key from the file matches with provided key or not
            if key == key_to_remove:
                result = True
                continue  

            # Append the line to updated_lines whether it was updated or not
            updated_lines.append(line)

        # Move the file pointer to the beginning of the file and truncate it
        file.seek(0)
        file.truncate()

        # Write the updated lines (excluding the line with the removed key-value pair) back to the file
        file.writelines(updated_lines)
        return result



# Update the value associated with a key.
def update_key(fileptr, key_to_update, new_value):
    # Create a temporary file to write the updated content
    temp_file = fileptr + "_temp"

    # Open the database file in read-write ('r+') mode
    with open(fileptr, 'r+') as file:
        # Open the temporary file in write ('w') mode
        # with open(temp_file, 'w') as temp:
            # Iterate through each line in the original file
            updated_lines = []
            result = False
            for line in file:
                # Split the line into key and value using ':' as the delimiter
                parts = line.strip().split(':')
                if len(parts) != 2:
                    continue
                key, _ = parts

                # Check if the key from the file matches the key to update
                if key == key_to_update:
                    result = True
                    # Update the line with the new value
                    # Replace the entire line
                    line = f"{key}:{new_value}\n"
                
                # Append the line to updated_lines whether it was updated or not
                updated_lines.append(line)

        
            # Move the file pointer to the beginning of the file and truncate it
            file.seek(0)
            file.truncate()

            # Write the updated lines (including the modified or new line) back to the end of the file
            file.writelines(updated_lines)
            return result



if __name__ == '__main__':
    main()
    
    

    