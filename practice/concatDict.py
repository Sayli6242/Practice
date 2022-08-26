"""
Write a Python script to concatenate following dictionaries to create a new one

Sample Dictionary :

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
def given_dict():

    team1= {1:10, 2:20}
    team2={3:30, 4:40}
    team3={5:50,6:60}
    
    
    return team1, team2, team3
    
def To_Concatenate_dictionary(team1, team2, team3):
    print("create temp dictonary to store all values")
    team = { }
    # loop over dict 1 keys 
    for key in team1:
        print(team1[key])
        team[key] = team1.get(key)
    for key in team2:
        print(team2[key])
        team[key] = team2.get(key)
    return team
        # 

        
    return team

def main():

    team1, team2, team3 = given_dict()
    
    team = To_Concatenate_dictionary(team1, team2, team3)

    print('concatenate string is:  ',team)

main()


