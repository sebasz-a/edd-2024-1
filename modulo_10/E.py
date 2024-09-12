votes = {}
voters = {} #para saber si un votante ha votado mas de una vez

while True:
    id, vote = tuple(map(int, input().split()))
    if id == 0:
        out = sorted(votes.items(), key=lambda x: (x[1], x[0]), reverse=True)
        for i in out:
            print(i[0], i[1], sep=' ')
        break

    if id not in voters:
        voters[id] = vote
        if vote not in votes:
            votes[vote] = 0
        votes[vote] += 1
    else:
        c_vote = voters[id]
        if c_vote == False:
            continue
        votes[c_vote] -= 1
        if votes[c_vote] == 0:
            del votes[c_vote]
        voters[id] = False
