# Functions used in the main.py file

from src.gameList import scores

def addPlayer(name, listToAddTo):
    if name in listToAddTo:
        print(name + " already exists")
    elif name.lower() == "greg":
        print("Greg cannot be added to the list... Complain to Sam if you have an issue")
    else:
        listToAddTo[name.lower()] = 1000

def recordGameManual(winners, losers, listToAdjust, c, d, l, t, gameName="[Game Title Not Given]"):
    omega = calcOmega(c, d, l, t)
    correct = True
    for winner in winners:
        if winner in listToAdjust:
            pass
        else:
            correct = False
    for loserSet in losers:
        for loser in loserSet:
            if loser in listToAdjust:
                pass
            else:
                correct = False
                
    
    if not correct:
        print("Error in game recording")
    else:
        # Log Tracking
        f = open("log.txt", "a")
        f.write("recordGameManual(" + str(winners) + "," + str(losers) + 
        "," + "masterList" + "," + str(c) + "," + str(d) + "," + 
        str(l) + "," + str(t) + "," + "gameName='" + gameName + "')\n")
        f.close()
        # End log tracking
        winSum = 0
        winVXP = 0
        # Calc winner VXP
        for winner in winners:
            winVXP += listToAdjust[winner]
        winVXP = winVXP/len(listToAdjust)
        # Loser section
        for loserSet in losers:
            tempLoseVXP = 0
            for loser in loserSet:
                tempLoseVXP += listToAdjust[loser]
            loseVXP = tempLoseVXP/len(loserSet)
            for loser in loserSet:
                deltaVXP = omega * (1/(1 + 10**((winVXP - loseVXP)/1000)))
                if deltaVXP < 1:
                    listToAdjust[loser] -= 1
                    winSum += 1
                else:
                    listToAdjust[loser] -= deltaVXP
                    winSum += deltaVXP
        # Winner section
        for winner in winners:
            listToAdjust[winner] += winSum/len(winners)

def calcOmega(c, d, _l, t):
    l = 0
    # Normalize t
    if _l == 1:
        l = 3
    elif _l == 2:
        l = 2
    elif _l == 3:
        l = 1
    elif _l == 4:
        l = 1/2
    else:
        l == 1/3
    
    return (c + d + t)*l

def printRanks(myDict):
    print("=====================================================================================")
    sorted_d = sorted(myDict, key=myDict.get, reverse=True)
    for r in sorted_d:
        print(r, myDict[r])
    print("=====================================================================================")

def verify(l):
    print("No. of players: " + str(len(l)))
    total = 0
    for k, v in l.items():
        total += v
    print("Total of all points: " + str(total))
    print("=====================================================================================")



def recordGameAuto(winners, losers, listToAdjust, t, gameName):
    test = scores.get(gameName)
    if (test == None):
        print("That game is not in gameList.Scores")
        return
    c = scores[gameName]["c"]
    d = scores[gameName]["d"]
    l = scores[gameName]["l"]

    omega = calcOmega(c, d, l, t)
    correct = True
    for winner in winners:
        if winner in listToAdjust:
            pass
        else:
            correct = False
    for loserSet in losers:
        for loser in loserSet:
            if loser in listToAdjust:
                pass
            else:
                correct = False
                
    
    if not correct:
        print("Error in game recording")
    else:
        # Log Tracking
        f = open("log.txt", "a")
        f.write("recordGameAuto(" + str(winners) + "," + str(losers) + 
        "," + "masterList" + "," + str(t) + "," + "gameName='" + gameName + "')\n")
        f.close()
        # End log tracking
        winSum = 0
        winVXP = 0
        # Calc winner VXP
        for winner in winners:
            winVXP += listToAdjust[winner]
        winVXP = winVXP/len(listToAdjust)
        # Loser section
        for loserSet in losers:
            tempLoseVXP = 0
            for loser in loserSet:
                tempLoseVXP += listToAdjust[loser]
            loseVXP = tempLoseVXP/len(loserSet)
            for loser in loserSet:
                deltaVXP = omega * (1/(1 + 10**((winVXP - loseVXP)/1000)))
                if deltaVXP < 1:
                    listToAdjust[loser] -= 1
                    winSum += 1
                else:
                    listToAdjust[loser] -= deltaVXP
                    winSum += deltaVXP
        # Winner section
        for winner in winners:
            listToAdjust[winner] += winSum/len(winners)