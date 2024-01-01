# import random


# letters = "abcdefghijklmnopqrstuvwxyz"
# aphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# for _ in range(5):
#     random_char = random.choice(letters + aphabets + numbers)
#     print(random_char)

import random

# import string


# def generate_random_string(length=5):
#     string = []
#     # characters to make random string
#     # characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

#     characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     # use random.choice to select random characters and join them to create string
#     for i in range(length):
#         z = random.choice(characters)
#         string.append(z)
#     print(string)

import sqlite3


# url_mapping = {}
# Connect to the SQLite database
conn = sqlite3.connect("url_mapping.db")
cursor = conn.cursor()


# Create a table to store the URL mapping
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS url_mapping (
        short_url TEXT PRIMARY KEY,
        long_url TEXT
    )
"""
)

conn.commit()


# class url(BaseModel):
#     url: str


def generate_random_string(length=5):
    string = ""
    # characters to make random string
    # characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # use random.choice to select random characters and join them to create string
    for i in range(length):
        random_string = random.choice(characters)
        string = string + random_string
    print(string)
    return string
    # con = sqlite3.connect("url_mapping.db")
    # cursor = con.cursor()
    # #  Check if it already exists in the database
    # cursor.execute("Insert INTO url_mapping(short_url) VALUES(?)", (string,))

    # count = cursor.fetchone()[0]
    # if count == 0:
    #     print(short_url)
    # con.commit()
    # con.close()


if __name__ == "__main__":
    generate_random_string(length=5)
