# fileptr = open("sample.txt","r")
# content = fileptr.read()
# print(content)

fileptr = open("sample.txt","r")
# fileptr.write("i am learning file handling as newbee")
# fileptr.write("\nTopics are open, read and write mode")
# fileptr.write("\nappend function")

print(fileptr.readlines(1))
# print(fileptr.readline())

fileptr.close()