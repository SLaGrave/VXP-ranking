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

recordGame(['dustin'],[['eric'], ['charlie'], ['casey']],masterList,5,4,2,9,gameName='Clash of Cultures')
recordGame(['sam', 'charlie', 'david', 'nate'],[['nathan', 'eric', 'abby', 'dryden', 'mady']],masterList,1,2,3,1,gameName='Secret Hitler')
recordGame(['nate', 'david', 'eric'],[['sam', 'mady', 'dryden', 'nathan']],masterList,1,2,3,1,gameName='Secret Hitler')
recordGame(['eric', 'david', 'nathan'],[['mady', 'dryden', 'sam', 'nate']],masterList,1,2,3,1,gameName='Secret Hitler')
recordGame(['casey'],[['dustin'], ['hamilton']],masterList,4,2,3,6,gameName='Stellar Leap')
recordGame(['eric'],[['sam'], ['jeremy'], ['nate'], ['max'], ['brady']],masterList,4,3,2,8,gameName='Dominare')
recordGame(['max'],[['david'], ['brady'], ['dryden']],masterList,2,1,4,1,gameName='Ascension')
recordGame(['eric'],[['dustin']],masterList,3,2,3,3,gameName='Clank')
recordGame(['charlie'],[['dustin'], ['eric']],masterList,2,3,2,1,gameName='Tokaido')
recordGame(['dustin'],[['jeremy'], ['eric'], ['nate']],masterList,2,2,3,2,gameName='Catan')
recordGame(['dryden', 'david'],[['mady', 'eric', 'brady', 'jeremy']],masterList,1,2,3,1,gameName='Secret Hitler')
recordGame(['dryden', 'david', 'brady', 'jeremy'],[['mady', 'eric']],masterList,1,2,3,1,gameName='Secret Hitler')
recordGame(['david', 'eric'],[['mady', 'dryden', 'brady', 'jeremy']],masterList,1,2,3,1,gameName='Secret Hitler')
recordGame(['eric', 'dustin'],[['mady']],masterList,1,2,3,1,gameName='Secrets')
recordGame(['eric', 'mady'],[['dustin']],masterList,1,2,3,1,gameName='Secrets')
recordGame(['eric'],[['dustin']],masterList,3,2,3,3,gameName='Clank')
recordGame(['david', 'nathan', 'brady'],[['sam', 'jeremy'], ['charlie']],masterList,1,2,3,1,gameName='Secrets')
recordGame(['heather'],[['casey']],masterList,1,1,5,1,gameName='Football Game')
recordGame(['eric'],[['dustin'], ['charlie'], ['max'], ['hamilton']],masterList,4,4,2,5,gameName='Shogun')
recordGame(['nathan'],[['brady'], ['dryden'], ['david'], ['mady']],masterList,2,1,4,2,gameName='Custom Heroes')
recordGame(['mady', 'david', 'nate', 'jeremy'],[['dryden', 'sam', 'brady', 'eric', 'nathan']],masterList,1,2,3,1,gameName='Secret Hitler')
recordGame(['brady', 'eric', 'nate', 'sam'],[['dryden', 'jeremy', 'david', 'mady', 'nathan']],masterList,1,2,3,1,gameName='Secret Hitler')



##################################################
# Code above here

printRanks(masterList)

# JSON masterList saveb
f = open("masterList.txt", "w")
f.write(json.dumps(masterList))
f.close()