# Complete the acmTeam function below.
def acmTeam(topic):
    
    teams = dict()

    for perm in combinations(topic, 2):
        #print(perm)
        bin_count = bin(int(perm[0],2) | int(perm[1],2))
        #print(bin_count)

        known_topics = str(bin_count).count('1')
        
        teams[known_topics] = teams.get(known_topics,0) + 1

    return(max(teams),teams[max(teams)])
