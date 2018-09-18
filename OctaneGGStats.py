# stats from Octane.gg
import RLDataSet
from decimal import Decimal
from scipy import stats

def learnStatistics():
	fullDataSet = RLDataSet.fullDataSet
	return fullDataSet

# finds the index of where a player's information is located
def indexFinder(query, fullDataSet):
	index = 0
	for person in fullDataSet:
		if person[0].lower() == query.lower():
			break	
		else:
			index = index + 1
	return index

def listStringToFloat(fullDataSet, statIndex):
	numList = []
	for member in fullDataSet:
		numList.append(member[statIndex])

	# for percentage column in list
	if "%" in numList[0]:
		index = 0
		for item in numList:
			numList[index] = item.strip("%")
			index += 1

	# for everything else
	numList = list(map(float, numList))
	return numList

def findPercentile(fullDataSet, query, statIndex):
	index = indexFinder(query,fullDataSet) # get player index
	currentStatistic = listStringToFloat(fullDataSet, statIndex) # converts list from string to float
	percentile = stats.percentileofscore(currentStatistic,float(fullDataSet[index][statIndex].strip("%")),kind="weak")
	percentile = str(round(percentile,2)) # rounds percentile
	return percentile

# returns the data given the name of a player, which is the query
def writeStatsSingle(query, fullDataSet):
	
	# finds where the player is located in the data set
	index = indexFinder(query, fullDataSet)
	underscoredString = query.replace(" ", "_")

	# strings for if player does not exist or if a player does exist
	if index >= len(fullDataSet):
		reply = "Invalid usage. Is your player misspelled or have you formatted incorrectly? \n\n"
		reply = reply + "---" + "\n\n"
		return reply
	else:
		reply = "# Statistics for [" + query + ":](https://octane.gg/player/" + underscoredString
		reply = reply + ")\n\n" + "Stats|" + query + "|Percentile|\n"
		reply = reply + ":---|---:|---:|" + "\n"
		reply = reply + "Games Played|" + fullDataSet[index][1] + "|" + findPercentile(fullDataSet,query,1) + "|\n"
		reply = reply + "Win Percentage|" + fullDataSet[index][2] + "|" + findPercentile(fullDataSet,query,2) + "|\n"
		reply = reply + "Average Score Per Game|" + fullDataSet[index][3] + "|" + findPercentile(fullDataSet,query,3) + "|\n"
		reply = reply + "Average Goals Per Game|" + fullDataSet[index][4] + "|" + findPercentile(fullDataSet,query,4) + "|\n"
		reply = reply + "Average Assists Per Game|" + fullDataSet[index][5] + "|" + findPercentile(fullDataSet,query,5) + "|\n"
		reply = reply + "Average Saves Per Game|" + fullDataSet[index][6] + "|" + findPercentile(fullDataSet,query,6) + "|\n"
		reply = reply + "Average Shots Per Game|" + fullDataSet[index][7] + "|" + findPercentile(fullDataSet,query,7) + "|\n"
		reply = reply + "---" + "\n\n"
		return reply

def writeStatsComparison(queryOne, queryTwo, fullDataSet):
	indexOne = indexFinder(queryOne, fullDataSet)
	underscoredStringOne = queryOne.replace(" ", "_")

	indexTwo = indexFinder(queryTwo, fullDataSet)
	underscoredStringTwo = queryTwo.replace(" ", "_")

	# index is longer than the length, that means a valid player was not found
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
	print(writeStatsComparison("Scrub Killa", "GarrettG", fullDataSet))
	# print(writeStatsSingle(input("Enter Player Name: "), fullDataSet))

if __name__ == "__main__":
	main()
