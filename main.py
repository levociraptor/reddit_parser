import praw
from datetime import datetime, timedelta
from collections import Counter

reddit = praw.Reddit(
    client_id="4qUO_BcWz0D8Xv1j0RlgUg",
    client_secret="R3BWsZxMWdaDXPR08-1w3U5EpNcDIA",
    redirect_uri="http://localhost:8080",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
)

list_of_post = []
list_of_authors = []
list_of_comments = []

datetime_now = datetime.now()
three_days_ago = datetime_now - timedelta(days=3)

subreddit = reddit.subreddit('learnpython')


count = 0
for post in subreddit.new(limit=None):
    post_datetime = datetime.fromtimestamp(post.created)
    count += 1

    if post_datetime <= three_days_ago:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('ITS OVER')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        break

    print(count)
    print(datetime.fromtimestamp(post.created))
    print(post.selftext)
    print()
    print(post.author)
    list_of_authors.append(post.author)
    list_of_comments += list(post.comments)
    print('######################################################################')

print()
print()
print()
print('Top authors')
counter_of_authors = Counter(list_of_authors)
for i in counter_of_authors.most_common(15):
    print(f'Author: {i[0].name}\nNumber of posts: {i[1]}')
    print()


print('comments')
list_of_comment_authors = [i.author for i in list_of_comments if i.author is not None]
counter_of_comments_author = Counter(list_of_comment_authors)
print(counter_of_comments_author)
for i in counter_of_comments_author.most_common(30):
    print(f'Author: {i[0].name}\nNumber of comments: {i[1]}')
    print()
