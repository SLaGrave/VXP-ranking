# Virgin Experience Points
import json
from src.functions import addPlayer, recordGameManual, printRanks, verify

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
# recordGameManual(["winner"], [["loser1", "loser2"], ["loser3"], ["loser4"]], masterList, 1, 1, 1, 1, "title")



##################################################
# Code above here

printRanks(masterList)
verify(masterList)

# JSON masterList saveb
f = open("masterList.txt", "w")
f.write(json.dumps(masterList))
f.close()