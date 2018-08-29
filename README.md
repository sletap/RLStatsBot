# RLStatsBot
A Rocket League Statistics bot that pulls information on Rocket League players from octane.gg by extracting information from HTML files. This bot is currently active and functional on the subreddits /r/RocketLeagueEsports and /r/RocketLeague

## Getting Started 
There are two different standalone files that are capable of extracting information. OctaneGGSelenium.py and OctaneGGStats.py. OctaneGGSelenium allows live updates and changes by taking the most current statistics, while OctaneGGStats reads data that was gathered before hand. 

The subreddit where the bot is active is currently /r/RocketLeagueEsports. This can be changed in line 23 of RLBot.py if desired

Comment IDs will be automatically be written in an external file which ensures a comment is not replied to more than once.

### Prerequisites
```
A reddit account with API access
A completed config file
PRAW
Python 3.0+
Beautiful Soup 4
Selenium with a webdriver
```
### Usage
start the bot with ```python3 RLBot.py```
now, when a user comments with ```!stats 'PLAYER NAME'``` The reddit bot will then fetch stats from a list, format it, and post it to the user
a user can also comment with ```!compare 'PLAYER ONE' 'PLAYER TWO'``` to compare statistics between two players

## File Rundown
* RLBot.py - Reddit bot that runs using information from OctaneGGStats.py
* OctaneGGStats.py - parses information from RLDataSet.py	
* OctaneGGSelenium.py	- parses information live from Octane.gg using Selenium
* RLDataSet.py - Player information that was obtained from OctaneGGSelenium.py that can be used in OctaneGGStats.py 
* config.py - example file for how the config should be set up using reddit API information

## Author
* Sahil Patel
