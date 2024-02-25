"""
1) 


"""

T = int(input())

for i in range(T):
    
    num_of_practice_matches = int(input())
    
    if num_of_practice_matches < 2:
        print("Unfit")  
    else:
       
        max_improvement = 0

        for i in range(num_of_practice_matches):
            
            goals_scored = int(input())
            max_improvement = max(max_improvement, goals_scored)
        if max_improvement == goals_scored:
            print("Unfit") 
        else:
            print("Fit")  
