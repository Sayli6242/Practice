
class Students:
    # pass
    def __init__(self,name,std,section ) :
        self.name = name
        self.std = std
        self.section = section

    def promoteToNextClass(self):
        self.std = promote(self.std)
    
    def getStd(self):
        return self.std


def promote(c):
    c+=1
    return c
        

student_1 = Students('sayli',11,'C')

student_1.promoteToNextClass()
print(student_1.getStd())