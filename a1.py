def evaluate(hand):
    rank=''
    suit=''
    result=''
    rankmatch=0
    suitmatch=0
    matchthree=False
    matchtwo=False
    cardval=0
    highest=False
    ranklist='23456789TJQKA'
    highestrank=''
    high=0
#for loops used to seperate ranks and suits into two seperate strings
    for i in range(0,10,2):
         rank+=hand[i]
    for j in range(1,10,2):
         suit+=hand[j]
#for loops used to test if the ranks are equal in the string "rank"
    for i in range(len(rank)):
        for j in range(len(rank)):
            if rank[i]==rank[j]:
#rankmatch variable used as a counter
                rankmatch+=1
#if statements to verify how many ranks are equal to each other based off of the rankmatch counter
        if rankmatch==4:
            result='four of a kind'
            return result
#matchthree and matchtwo will be used to determine whether or not the hand is of case (2),(4), or (5)
        if rankmatch==3:
            matchthree=True
        if rankmatch==2:
            matchtwo=True
#resets rankmatch in order to check for the next rank in the string
        rankmatch=0
#if statements to determine if the hand is of case (2),(4), or (5)
    if matchthree and matchtwo:
        result='full house'
        return result
    elif matchthree and not matchtwo:
        result='three of a kind'
        return result
    elif not matchthree and matchtwo:
        result='pair'
        return result
#for loops used to test for equal suits in the same format of the loops used for testing ranks
    for i in range(len(suit)):
        for j in range(len(suit)):
            if suit[i]==suit[j]:
                suitmatch+=1
#Checks if suitmatch counter is equal to 5 which would indicate a flush
        if suitmatch==5:
            result='flush'
            return result
        suitmatch=0
#for loops used to match the rank of the card in hand to the rank in ranklist which would help in determining the highest rank
    for i in range(len(rank)):
        for j in range(len(ranklist)):
            if rank[i]==ranklist[j]:
#assigns cardval to a numerical value
                cardval=j
                if not highest:
#makes the first rank the initial highest rank
                    highest=True
                    highestrank=ranklist[j]
                    high=cardval
                else:
#checks if the the rank is higher than the current highest rank card in hand
                    if cardval>high:
                        highestrank=ranklist[j]
                        high=cardval
    result='high'
#prints the highest rank
    print(highestrank,end=' ')
    return result



#calls on function and prints out result
print(evaluate('Qs7s2s4s5s'))
print(evaluate('7h8hKsTs8s'))
print(evaluate('2h4d2d4s4c'))
print(evaluate('KsKhKc8sKd'))
print(evaluate('3s9hTh9s9d'))
print(evaluate('2s8hThQs9d'))

