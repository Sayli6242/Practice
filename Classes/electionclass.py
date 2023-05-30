class election:
    def __init__(self):
        self.__candidate_lst =[ ]
        # self.voters_lst =[ ]
        self.__votes = [ ]


    # constructor

    # properties

    # methods
    def candidate_register(self):
        for i in range(4):
            x = input('enter candidate name')
            self.__candidate_lst.append(x)
            print(self.__candidate_lst)

    def collect_votes(self):
        for i in range(10):
            y = input('enter votes for candidates')
            self.__votes.append(y)
            print(self.__votes)
    
    def calculate_votes():
        pass

  
e = election()

# e = election()

print(e.candidate_register())



