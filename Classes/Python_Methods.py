

# create a class
class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        area = self.length * self.breadth
        print("the area is: ",area)

# create object of Room class
study_room = Room()

# assign values to all attribures
study_room.length = 35
study_room.breadth = 20

# access method inside class
study_room.calculate_area()

