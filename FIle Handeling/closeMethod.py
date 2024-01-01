#  opens the file sample.txt in read mode

fileptr = open("sample.txt")

if fileptr:
    print("file is opened successfully")


# closes the opened file

fileptr.close()

if fileptr:
    print('file closed successfully')