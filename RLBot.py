# Rocket League Stats bot that uses data from Octane.gg
import praw
import config
import os
import time
import OctaneGGStats

commentFile = "CommentsRepliedTo.txt"

# logs the bot in
# credentials are stored in an external file (config)
def initializeBot():
	login = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "/u/Sahil0719's RL Bot")
	return login

# what comment to search for on what subreddit, and what to reply with

# EXPERIMENT: or comment in Bot.subreddit('Test').comments(limit=100):
def runBot(Bot, CommentsRepliedTo, fullDataSet):
	for comment in Bot.subreddit('Test').comments(limit=100):

		# brings up the stats of one player
		if "!stats" in comment.body and comment.id not in CommentsRepliedTo and comment.author != Bot.user.me():
			body = comment.body[comment.body.find("!stats"):]
			body = body.replace("‘","'").replace("’","'")
			body = body.split("'",2)
			body.append("placeholder")
			player = body[1]

			reply = OctaneGGStats.writeStatsSingle(player, fullDataSet)
			comment.reply(reply + "\n ^(stats are provided by) ^[Octane.gg](https://octane.gg/stats/players/career/#main), ^(this bot was created by /u/Sahil0719)"
				+ "\n\n    usage:\n        !stats 'Player Name' (apostrophes are required)")

			print("a stats reply has been made for " + str(comment.author))

			CommentsRepliedTo.append(comment.id)
			with open (commentFile, "a") as f:
				f.write(comment.id + "\n")

		# compares the stats of two players
		if "!compare" in comment.body and comment.id not in CommentsRepliedTo and comment.author != Bot.user.me():
			body = comment.body[comment.body.find("!compare"):]
			body = body.replace("‘","'").replace("’","'")
			body = body.split("'",4)
			body = list(filter(None, body))
			body.append("placeholder")

			del body[2]
			body.append("placeholder")
			playerOne = body[1]
			playerTwo = body[2]

			reply = OctaneGGStats.writeStatsComparison(playerOne,playerTwo,fullDataSet)
			comment.reply(reply + "\n ^(stats are provided by) ^[Octane.gg](https://octane.gg/stats/players/career/#main), ^(this bot was created by /u/Sahil0719)"
				+ "\n\n    usage:\n        !compare 'Player Name One' 'Player Name Two' (apostrophes are required)")

			print("a comparison reply has been made for " + str(comment.author))

			CommentsRepliedTo.append(comment.id)
			with open (commentFile, "a") as f:
				f.write(comment.id + "\n")

# this helps make sure a comment is not replied to more than once
def getSavedComments():
	if not os.path.isfile(commentFile):
		comments_replied_to = []
	else:
		with open(commentFile, "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")

	return comments_replied_to

def main():
	RedditBot = initializeBot()
	CommentsRepliedTo = getSavedComments()
	fullDataSet = OctaneGGStats.learnStatistics()
	print("Currently Logging in \n")

	while True:
		print("Searching for Comments")
		runBot(RedditBot,CommentsRepliedTo,fullDataSet)
		time.sleep(10)

if __name__ == "__main__":
	main()
