# Get Required Library

import threading
from builtins import len, str
from threading import *
import time

# Create a Dictionary to store the Key-Value Pair
db = {}


# Function Definition for Create Operation

def create(key, value, timeout=0):
    if key in db:
        print("Error: this key already exists")
    else:
        if key.isalpha():
            if len(db) < (1020*1024*1024) and value <= (16*1024*1024):
                if timeout == 0:
                    data = [value, timeout]
                else:
                    data = [value, time.time() + timeout]
                if len(key) <= 32:
                    db[key] = data
            else:
                print("Error: Memory limit exceeded!")
        else:
            print(
                "Error: Invalid KeyName! KeyName must contain only alphabets")


# Function Definition for Read Operation

def read(key):
    if key not in db:
        print("Sorry! given key does not exist in database.")
    else:
        data = db[key]
        if data[1] != 0:
            if time.time() < data[1]:
                info = str(key) + ":" + str(data[0])
                return info
            else:
                print("Error: Time-To-Live of", key, "has Expired")
        else:
            info = str(key) + ":" + str(data[0])
            return info


# Function Definition for Delete Operation

def delete(key):
    if key not in db:
        print("Sorry! given key does not exist in database.")
    else:
        data = db[key]
        if data[1] != 0:
            if time.time() < data[1]:
                del db[key]
                print("key is successfully deleted")
            else:
                print("Error: Time-To-Live of", key, "has Expired")
        else:
            del db[key]
            print("key is successfully deleted")
