# stats from Octane.gg, writes list to RLDataSet.py
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
import time

# Parses data using Beautiful Soup 4 and return a list with all needed information
def learnStatistics():
	fullDataSet = [] # this is where all the information will be stored
	url = "https://octane.gg/stats/players/career/#main"
	options = Options()
	options.add_argument('--headless')
	browser = webdriver.Chrome(chrome_options=options)

	browser.get(url)
	time.sleep(3) # it takes time to load the page, which is also why selenium is used

	html = browser.page_source
	soup = BeautifulSoup(html, 'html.parser')

	# finds the table and extract the data one row at a time into a python list
	table = soup.find("section", {"id": "#main"})
	table_body = table.find('tbody')
	rows = table_body.find_all('tr')
	for row in rows:
		cols = row.find_all('td')
		cols = [element.text.strip() for element in cols]
		fullDataSet.append([element for element in cols if element])
	
	fullDataSet = list(filter(None, fullDataSet)) # gets rid of empty elements if any
	return fullDataSet

# example run for testing outside of a reddit instance
def main():
	fullDataSet = learnStatistics()
	fileWrite = open("RLDataSet.py", "w")
	fileWrite.write("fullDataSet = " + str(fullDataSet))

if __name__ == "__main__":
	main()
