import praw
import json

# Opening JSON file
f = open('client_secrets.json')
# returns JSON object as 
# a dictionary
data = json.load(f)


reddit = praw.Reddit(
    client_id=data['client_id'],
    client_secret=data['client_secret'],
    user_agent=data['user_agent']
)

url = "https://www.reddit.com/r/esist/comments/6g18xv/theres_so_much_more_about_trump_to_investigate/"
submission = reddit.submission(url=url)

#print(submission.comments[1].body)


for comment in submission.comments:
    print(comment.body)
