
a = [1, 2, 3]
try: 
    print ("Second element = %d" %(a[1]))

    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))

    print ("No error occurred")
  
except ZeroDivisionError as e:
    print ("An error occurred",e)
except IndexError as e:
    print ("An error occurred",e)