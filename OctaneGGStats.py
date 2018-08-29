# stats from Octane.gg, static implementation
import RLDataSet
from decimal import Decimal

# Parses data using Beautiful Soup 4 and return a list with all needed information
def learnStatistics():
	fullDataSet = RLDataSet.fullDataSet # this is where all the information will be stored
	return fullDataSet

# creates a list of only players so we can search through them when a user calls for a player
def makePlayersList(fullDataSet):
	players = [] # this is where we will index players
	for player in fullDataSet:
		players.append(player[0])

	return players

def indexFinder(query, players):
	index = 0
	for person in players:
		if person.lower() == query.lower():
			break	
		else:
			index = index + 1
	return index

# returns the data given the name of a player, which is the query
def writeStatsSingle(query, players, fullDataSet):
	# finds where the player is located in the data set
	index = indexFinder(query, players)
	underscoredString = query.replace(" ", "_")

	# strings for if player does not exist or if a player does exist
	if index >= len(fullDataSet):
		reply = "Invalid usage. Is your player misspelled or have you formatted incorrectly? \n\n"
		reply = reply + "---" + "\n\n"
		return reply
	else:
		reply = "# Statistics for [" + query + ":](https://octane.gg/player/" + underscoredString
		reply = reply + ")\n\n" + "Stats|" + query + "|\n"
		reply = reply + ":---|---:|" + "\n"
		reply = reply + "Games Played|" + fullDataSet[index][1] + "|\n"
		reply = reply + "Win Percentage|" + fullDataSet[index][2] + "|\n"
		reply = reply + "Average Score Per Game|" + fullDataSet[index][3] + "|\n"
		reply = reply + "Average Goals Per Game|" + fullDataSet[index][4] + "|\n"
		reply = reply + "Average Assists Per Game|" + fullDataSet[index][5] + "|\n"
		reply = reply + "Average Saves Per Game|" + fullDataSet[index][6] + "|\n"
		reply = reply + "Average Shots Per Game|" + fullDataSet[index][7] + "|\n"
		reply = reply + "---" + "\n\n"
		return reply

def writeStatsComparison(queryOne, queryTwo, players, fullDataSet):
	indexOne = indexFinder(queryOne, players)
	underscoredStringOne = queryOne.replace(" ", "_")

	indexTwo = indexFinder(queryTwo, players)
	underscoredStringTwo = queryTwo.replace(" ", "_")

	if indexOne >= len(fullDataSet) or indexTwo >= len(fullDataSet):
		reply = "Invalid usage, are either of your players misspelled or have you formatted incorrectly? \n\n"
		reply = reply + "---" + "\n\n"
		return reply
	else:
		reply = "# Statistics for [" + queryOne + "](https://octane.gg/player/" + underscoredStringOne + ")"
		reply = reply +" and [" + queryTwo + ":](https://octane.gg/player/" + underscoredStringTwo
		reply = reply + ")\n\n" + "Stats|" + queryOne + "|" + queryTwo + "|Differential|\n"
		reply = reply + ":---|:---:|:---:|---:|" + "\n"
		reply = reply + "Games Played|" + fullDataSet[indexOne][1] + "|" + fullDataSet[indexTwo][1] + "|"
		reply = reply + str(Decimal(fullDataSet[indexOne][1]) - Decimal(fullDataSet[indexTwo][1])) + "|\n"
		reply = reply + "Win Percentage|" + fullDataSet[indexOne][2] + "|" + fullDataSet[indexTwo][2] + "|"
		reply = reply + str(Decimal(fullDataSet[indexOne][2].strip('%')) - Decimal(fullDataSet[indexTwo][2].strip('%'))) + "%	|\n"
		reply = reply + "Average Score Per Game|" + fullDataSet[indexOne][3] + "|" + fullDataSet[indexTwo][3] + "|"
		reply = reply + str(Decimal(fullDataSet[indexOne][3]) - Decimal(fullDataSet[indexTwo][3])) + "|\n"
		reply = reply + "Average Goals Per Game|" + fullDataSet[indexOne][4] + "|" + fullDataSet[indexTwo][4] + "|"
		reply = reply + str(Decimal(fullDataSet[indexOne][4]) - Decimal(fullDataSet[indexTwo][4])) + "|\n"
		reply = reply + "Average Assists Per Game|" + fullDataSet[indexOne][5] + "|" + fullDataSet[indexTwo][5] + "|"		
		reply = reply + str(Decimal(fullDataSet[indexOne][5]) - Decimal(fullDataSet[indexTwo][5])) + "|\n"
		reply = reply + "Average Saves Per Game|" + fullDataSet[indexOne][6] + "|" + fullDataSet[indexTwo][6] + "|"
		reply = reply + str(Decimal(fullDataSet[indexOne][6]) - Decimal(fullDataSet[indexTwo][6])) + "|\n"
		reply = reply + "Average Shots Per Game|" + fullDataSet[indexOne][7] + "|" + fullDataSet[indexTwo][7] + "|"
		reply = reply + str(Decimal(fullDataSet[indexOne][7]) - Decimal(fullDataSet[indexTwo][7])) + "|\n"
		reply = reply + "---" + "\n\n"
		return reply

# example run for testing outside of a reddit instance
def main():
	fullDataSet = learnStatistics()
	players = makePlayersList(fullDataSet)
	print(writeStatsComparison("Fireburner", "GarrettG", players, fullDataSet))
	# print(writeStatsSingle("Scrub Killa", players, fullDataSet))

if __name__ == "__main__":
	main()
