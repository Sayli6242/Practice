

# class database:

#     def __init__(self,age):
        
#         self.age = age

# class person(database):

#     if age > 15:

#         print('age')
#     else:

#         print('year')


# if __name__ == '__main__':
#     database()

# z = z.person(10)

employee_position = {1:'employee_id',2:'posiotion',3:'skills'}
for key,value in employee_position.items():
    print(key,value)
z = int(input('enter choice: '))
if z == 1:
    print(z)
if z == 2:
    position =  {1:'developer',2:'analyst',3:'tester',4:'manager'}
    for key,value in position.items():
        print(key,value)
