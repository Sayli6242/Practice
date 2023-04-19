# write data to a text file using python!



name = open('phone.txt', 'a')
name.write(input('name:  '))
name.close()



# name = open('phone.txt','w')
# username = ['sayli','kajal','sweety']
# contacts = ['2541','6463','46646464']
# for i in range(0, 6):
#     entry = username[i] + '-' + str(contacts[i])+ '\n'
#     name.write(entry)

name.close()