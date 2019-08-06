# Changes I would make looking at this project a year later
Looking back on this project with the knowledge that I have now a year later (Reading this as of August 2019), I would try to use something like AWS Lambdas that are triggered by keywords which would gather data from a database to write back to the user. This would save on server costs as it doesn't make sense to spin up a server running only this small script. I may come back to this project in the future and try to implement it that way and re-release it

# RLStatsBot
A Rocket League Statistics bot that pulls information on Rocket League players from octane.gg by extracting information from HTML files. This bot is currently active and functional on the subreddits /r/RocketLeagueEsports and /r/RocketLeague. An example comment can be seen  here: https://goo.gl/YqvNBr

## Getting Started 
Run ```python3 RLBot.py``` to start the bot. If desired, OctangeGGSelenium can be run to get an updated data set.  

The subreddit where the bot is active is currently /r/RocketLeagueEsports and /r/RocketLeague. This can be changed in line 23 of RLBot.py if desired

```!stats 'PLAYER NAME'``` or  ```!compare 'PLAYER ONE' 'PLAYER TWO'``` can be used on either subreddit to get a response

Comment IDs will be automatically be written in an external file to ensure a comment is not replied to more than once.

### Prerequisites to run this bot yourself
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

now, when a user comments with ```!stats 'PLAYER NAME'``` The reddit bot will then fetch stats from a list, format it, and post it to the user.

a user can also comment with ```!compare 'PLAYER ONE' 'PLAYER TWO'``` to compare statistics between two players

## File Rundown
* RLBot.py - Reddit bot that runs using information from OctaneGGStats.py
* OctaneGGStats.py - reads and formats information from RLDataSet.py	
* OctaneGGSelenium.py	- gathers the data set from Octane.gg using Selenium
* RLDataSet.py - Player information that was obtained from OctaneGGSelenium.py that can be used in OctaneGGStats.py 
* config.py - example file for how the config should be set up to use in PRAW

## Author
* Sahil Patel
