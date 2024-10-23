import praw

from datetime import datetime, timedelta
from collections import Counter

from config import load_config


def find_subreddit_posts(reddit: praw.Reddit, days: int, subreddit_name: str) -> list:
    datetime_now = datetime.now()
    n_days_ago = datetime_now - timedelta(days=days)
    subreddit = reddit.subreddit(subreddit_name)

    list_of_post = []

    for post in subreddit.new(limit=None):
        post_datetime = datetime.fromtimestamp(post.created)
        list_of_post.append(post)

        if post_datetime <= n_days_ago:
            return list_of_post


def console_output_post(post) -> None:
    post_author = post.selftext
    post_date = datetime.fromtimestamp(post.created)

    print(f'\nPost author: {post_author}')
    print(f'\nPost date: {post_date}')
    print(post.selftext)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')


def console_output_top_posts_authors(list_of_authors: list) -> None:
    print('AUTHORS')
    counter_of_authors = Counter(list_of_authors)
    for i in counter_of_authors.most_common(15):
        print(f'Author: {i[0].name}\nNumber of posts: {i[1]}')
        print()


def console_output_top_comments_authors(list_of_comments: list) -> None:
    print('COMMENTS')
    list_of_comment_authors = [i.author for i in list_of_comments if i.author is not None]
    counter_of_comments_author = Counter(list_of_comment_authors)
    for i in counter_of_comments_author.most_common(30):
        print(f'Author: {i[0].name}\nNumber of comments: {i[1]}')
        print()


def main() -> None:
    config = load_config()
    reddit = praw.Reddit(
        client_id=config.client_id,
        client_secret=config.client_secret,
        redirect_uri=config.redirect_uri,
        user_agent=config.user_agent
    )

    list_of_posts = find_subreddit_posts(reddit, 3, 'learnpython')

    list_of_authors = []
    list_of_comments = []

    for post in list_of_posts:
        list_of_authors.append(post.author)
        list_of_comments.extend(post.comments)
        console_output_post(post)

    console_output_top_posts_authors(list_of_authors)
    console_output_top_comments_authors(list_of_comments)


if __name__ == '__main__':
    main()
