"""
Given an array of names of candidates in an election.
 A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. 

Input :  votes =["john", "john", "mackie", 
                    "john", "john", "mackie", 
                    "lamie", "lamie", "john",
                    "john", "lamie", "john", 
                    "john"];
Output : John

SPECIAL_CASE: If there is tie, print a lexicographically smaller name.
answer steps:
what is given
- votes array 


"""
def to_find_vote_count_and_highest_votes(votes):
    vote_count = {}
    # key is candidate name and value is count of votes.

    # apply for loop to intrate each vote in list.
    for vote in votes:
        print(vote)
        # create key , value in dictionary vote count. where key is candidate name and value is vote count.
        existing_val = vote_count.get(vote,0)
        vote_count[vote] = existing_val+1
          #  calculate min max in dict
        return vote_count()


def main():
    # list of votes
    votes =["john", "john", "mackie", 
                    "john", "john", "mackie", 
                    "lamie", "lamie", "john",
                    "john", "lamie", "john", 
                    "john"]
                    
    print("candidate who receives highest votes: ",votes)
    
  

main()