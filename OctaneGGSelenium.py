# stats from Octane.gg, Live Selenium implementation
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
import time

# Parses data using Beautiful Soup 4 and return a list with all needed information
def learnStatistics():
	url = "https://octane.gg/stats/players/career/#main"
	options = Options()
	options.add_argument('--headless')
	browser = webdriver.Chrome(chrome_options=options)
	browser.get(url)
	time.sleep(3)
	fullDataSet = [] # this is where all the information will be stored

	html = browser.page_source
	soup = BeautifulSoup(html, 'html.parser')

	table = soup.find('table', attrs={'class':'vuetable ui blue selectable celled stackable attached table'})
	table_body = table.find('tbody')
	rows = soup.find_all('tr')

	for row in rows:
		cols = row.find_all('td')
		cols = [element.text.strip() for element in cols]
		fullDataSet.append([element for element in cols if element])
	
	fullDataSet = list(filter(None, fullDataSet)) # gets rid of empty elements
	# print(fullDataSet)
	return fullDataSet

# creates a list of only players so we can search through them when a user calls for a player
def makePlayersList(fullDataSet):
	players = [] # this is where we will index players
	for player in fullDataSet:
		players.append(player[0])

	return players

# returns the data given the name of a player, which is the query
def writeStats(query, players, fullDataSet):
	# finds where the player is located in the data set
	index = 0
	for person in players:
		if person.lower() == query.lower():
			break	
		else:
			index = index + 1

	# strings for if player does not exist or if a player does exist
		if index >= len(fullDataSet):
			reply = query + " is not available on octane.gg. Is your player misspelled?"
		return reply
	else:
		reply = "# Statistics for " + query + ":" + "\n\n"
		reply = reply + query + "|Stats|" + "\n"
		reply = reply + "---|---:|" + "\n"
		reply = reply + "Games Played|" + fullDataSet[index][1] + "|\n"
		reply = reply + "Win Percentage|" + fullDataSet[index][2] + "|\n"
		reply = reply + "Average Score Per Game|" + fullDataSet[index][3] + "|\n"
		reply = reply + "Average Goals Per Game|" + fullDataSet[index][4] + "|\n"
		reply = reply + "Average Assists Per Game|" + fullDataSet[index][5] + "|\n"
		reply = reply + "Average Saves Per Game|" + fullDataSet[index][6] + "|\n"
		reply = reply + "Average Shots Per Game|" + fullDataSet[index][7] + "|\n"
		reply = reply + "---" + "\n\n"
		return reply

# example run for testing outside of a reddit instance
def main():
	fullDataSet = learnStatistics()
	# players = makePlayersList(fullDataSet)
	# print(writeStats("Fireburner", players, fullDataSet))

if __name__ == "__main__":
	main()