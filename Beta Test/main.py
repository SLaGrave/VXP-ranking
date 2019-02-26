# Virgin indeX Point system
import json
from src.functions import addPlayer, recordGame, printRanks

# Variable definitions
masterList = {}

# JSON masterList setup
f = open("masterList.txt", "r")
for line in f:
    masterList = json.loads(line)
f.close()

# Code below here
##################################################
# Examples:
# addPlayer("name", masterList)
# recordGame(["winner"], [["loser1", "loser2"], ["loser3"], ["loser4"]], masterList, 1, 1, 1, 1, "title")


##################################################
# Code above here

printRanks(masterList)

# JSON masterList saveb
f = open("masterList.txt", "w")
f.write(json.dumps(masterList))
f.close()