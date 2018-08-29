# Rocket League Stats bot that uses data from Octane.gg
import praw
import config
import os
import time
import OctaneGGStats

commentFile = "CommentsRepliedTo.txt"

# logs the bot in
# credentials are stored in an external file (config) for security
def initializeBot():
	print("Currently Logging in \n")
	login = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "/u/Sahil0719's RL Bot")
	return login

# what comment to search for on what subreddit, and what to reply with
def runBot(Bot, CommentsRepliedTo, fullDataSet, players):
	for comment in Bot.subreddit('RocketLeagueEsports').comments(limit=100):
		if "!stats" in comment.body and comment.id not in CommentsRepliedTo and comment.author != Bot.user.me():
			body = comment.body[comment.body.find("!stats"):]
			body = body.replace("‘","'").replace("’","'")
			body = body.split("'",2)
			body.append("placeholder")
			player = body[1]

			reply = OctaneGGStats.writeStats(player, players, fullDataSet)
			comment.reply(reply + "\n ^(stats are provided by) ^[Octane.gg](https://octane.gg/stats/players/career/#main), ^(this bot was created by /u/Sahil0719)"
				+ "\n\n    usage:\n        !stats 'Player Name' (These should be the first words of the comment)")

			print("a reply has been made for " + str(comment.author))

			CommentsRepliedTo.append(comment.id)
			with open (commentFile, "a") as f:
				f.write(comment.id + "\n")

# this helps make sure a comment is not replied to more than once
def get_saved_comments():
	if not os.path.isfile(commentFile):
		comments_replied_to = []
	else:
		with open(commentFile, "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")

	return comments_replied_to

def main():
	RedditBot = initializeBot()
	CommentsRepliedTo = get_saved_comments()
	fullDataSet = OctaneGGStats.learnStatistics()
	players = OctaneGGStats.makePlayersList(fullDataSet)

	while True:
		print("Searching for Comments")
		runBot(RedditBot,CommentsRepliedTo,fullDataSet,players)
		time.sleep(10)

if __name__ == "__main__":
	main()
