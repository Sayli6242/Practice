




def electionsWinners(votes, k):
    winner  = 0
    for i in range(0,len(votes)):
        newVotes = list(votes)
        newVotes[i] += k
        if newVotes[i] == max(newVotes) and newVotes.count(newVotes[i])==1:
            winner += 1
    
    return winner



def main():
    votes =["john", "john", "mackie", 
                    "john", "john", "mackie", 
                    "lamie", "lamie", "john",
                    "john", "lamie", "john", 
                    "john"]
    electionsWinners(votes, k)
main()
