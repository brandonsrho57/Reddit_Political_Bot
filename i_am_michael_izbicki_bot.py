# importing necessary libraries
import praw
import random
import datetime
from textblob import TextBlob

# generate comments to post
def generate_comment_0():
    joenames = ['Joe', 'Biden', 'Joe Biden', 'Joseph Biden', 'Joey', 'Joseph', 'Joseph Robinette Biden Jr.', "Obama's Vice President"]
    joebiden = random.choice(joenames)
    americanames = ['America', 'USA', 'United States of America', 'Murica', 'States', 'US']
    america = random.choice(americanames)
    legislation = ['legislation', 'bills', 'executive orders', 'laws']
    document = random.choice(legislation)
    econ = ['economy', 'bubble', 'stock market', 'financial world']
    economy = random.choice(econ)
    vp = ['VP', 'vice president', 'second commander in chief', 'president #2']
    vicepresident = random.choice(vp)

    text = joebiden + " really cares about " + america + ".It's shown by the " + document + " he's passed during his tenure as " + vicepresident + ". I mean, who doesn't like him? While he was in office with Obama, he helped get the " + economy + " get back in shape after the 2008 recession."
    return text

def generate_comment_1():
    donaldnames = ['Donald', 'Trump', 'Donald Trump', 'Donald J. Trump', 'Donald John Trump', 'The President', 'Businessman Trump', 'Trumpster']
    donaldtrump = random.choice(donaldnames)
    americanames = ['America', 'USA', 'United States of America', 'Murica', 'States', 'US']
    america = random.choice(americanames)
    foreigncountrynames = ['China', 'Russia', 'Mexico', 'Canada', 'North Korea']
    foreigncountry = random.choice(foreigncountrynames)
    econ = ['economy', 'bubble', 'stock market', 'financial world']
    economy = random.choice(econ)
    covid = ['virus', 'Wuhan Virus', 'coronavirus', 'corona', 'Covid-19']
    virus = random.choice(covid)

    text = donaldtrump + " is literally the BEST. He will keep " + america + " great! He made our " + economy + " great and will do it again! We were just flubbed by the " + virus + ". He takes no crap from " + foreigncountry + "."
    return text

def generate_comment_2():
    joenames = ['Joe', 'Biden', 'Joe Biden', 'Joseph Biden', 'Joey', 'Joseph', 'Joseph Robinette Biden Jr.', "Obama's Vice President"]
    joebiden = random.choice(joenames)
    donaldnames = ['Donald', 'Trump', 'Donald Trump', 'Donald J. Trump', 'Donald John Trump', 'The President', 'Businessman Trump', 'Trumpster']
    donaldtrump = random.choice(donaldnames)
    choose = ['vote', 'choose', 'pick', 'select', 'take']
    vote = random.choice(choose)
    jobs = ['blue-collar worker', 'white-collar worker', 'Walmart employee', 'programmer', 'student']
    job = random.choice(jobs)
    office = ['the White House', 'the Oval Office', 'office', 'the house']
    wh = random.choice(office)

    text = "Although both " + joebiden + " and " + donaldtrump + " are decent candidates, I'm inclined to " + vote + " " + joebiden + " because I'm just a " + job + " who just wants things to go back to what they were. If " + donaldtrump + " gets another 4 years in the " + wh + ", I'm afraid of the division."
    return text

# Last 3 will be unsupportive messages
def generate_comment_3():
    joenames = ['Joe', 'Biden', 'Joe Biden', 'Joseph Biden', 'Joey', 'Joseph', 'Joseph Robinette Biden Jr.', "Obama's Vice President"]
    joebiden = random.choice(joenames)
    donaldnames = ['Donald', 'Trump', 'Donald Trump', 'Donald J. Trump', 'Donald John Trump', 'The President', 'Businessman Trump', 'Trumpster']
    donaldtrump = random.choice(donaldnames)
    foreigncountrynames = ['China', 'Russia', 'Mexico', 'Canada', 'North Korea']
    foreigncountry = random.choice(foreigncountrynames)
    nicknames = ['Crooked Hillary', 'Rocket Man', 'Phony Kamala', 'Cryin Chuck', 'Pocohontas']
    nickname = random.choice(nicknames)
    prez = ['president', 'POTUS', 'President of the United States', 'prez', 'United States President']
    president = random.choice(prez)
    joenicknames = ['Sleepy Joe', 'Crooked Joe', 'Basement Joe', 'Joe-ker', 'Joe mama']
    biden = random.choice(joenicknames)

    text = "If you choose " + joebiden + " as the next " + president + ", I just want to let you know that you're publicly supporting " + nickname + " to run the country, not " + biden + ". Nobody has been harder on " + foreigncountry + " than " + donaldtrump + "."
    return text

def generate_comment_4():
    donaldnames = ['Donald', 'Trump', 'Donald Trump', 'Donald J. Trump', 'Donald John Trump', 'The President','Businessman Trump', 'Trumpster']
    donaldtrump = random.choice(donaldnames)
    foreigncountrynames = ['China', 'Russia', 'Mexico', 'Canada', 'North Korea']
    foreigncountry = random.choice(foreigncountrynames)
    covid = ['virus', 'Wuhan Virus', 'coronavirus', 'corona', 'Covid-19']
    virus = random.choice(covid)
    prez = ['president', 'POTUS', 'President of the United States', 'prez', 'United States President']
    president = random.choice(prez)
    office = ['the White House', 'the Oval Office', 'office', 'the house']
    wh = random.choice(office)

    text = donaldtrump + " has been in " + wh + " 4 years too long. He's a political lightweight and can't handle the job as the " + president + ". Just look what happened during the " + virus + ". " + foreigncountry + " literally hates his guts and we have to have good relations with them."
    return text

def generate_comment_5():
    joenames = ['Joe', 'Biden', 'Joe Biden', 'Joseph Biden', 'Joey', 'Joseph', 'Joseph Robinette Biden Jr.', "Obama's Vice President"]
    joebiden = random.choice(joenames)
    donaldnames = ['Donald', 'Trump', 'Donald Trump', 'Donald J. Trump', 'Donald John Trump', 'The President', 'Businessman Trump', 'Trumpster']
    donaldtrump = random.choice(donaldnames)
    americanames = ['America', 'USA', 'United States of America', 'Murica', 'States', 'US']
    america = random.choice(americanames)
    foreigncountrynames = ['China', 'Russia', 'Mexico', 'Canada', 'North Korea']
    foreigncountry = random.choice(foreigncountrynames)
    jobs = ['blue-collar worker', 'white-collar worker', 'Walmart employee', 'programmer', 'student']
    job = random.choice(jobs)

    text = "Both candidates are straight garbage. " + joebiden + " is going senile while " + donaldtrump + " looks like an absolute clown on Twitter. The way we're headed, the " + america + " won't be around for much longer. I'd honestly rather have " + foreigncountry + " running this country because I, as a " + job + ", hate them."
    return text

def generate_comment():
    for i in range(1):
        options = [0, 1, 2, 3, 4, 5]
        choice = random.choice(options)
        if choice == 0:
            return generate_comment_0()
        elif choice == 1:
            return generate_comment_1()
        elif choice == 2:
            return generate_comment_2()
        elif choice == 3:
            return generate_comment_3()
        elif choice == 4:
            return generate_comment_4()
        elif choice == 5:
            return generate_comment_5()

# connect to the submission with the bot
reddit = praw.Reddit('i_am_michael_izbicki_bot')
# reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jmarit/rudy_giuliani_is_my_father_please_everyone_vote/'
submission = reddit.submission(url=reddit_debate_url)

while True:
    print()
    print('New Iteration At: ', datetime.datetime.now())
    print('Title of Submission: ', submission.title)
    print('URL of Submission: ', submission.url)
    submission.comments.replace_more(limit=None)

    # Task 0 (2 points)
    all_comments = []
    for comment in submission.comments.list():
        all_comments.append(comment)

    print('Number of Comments: ', len(all_comments))

    # Task 1 (2 points)
    not_my_comments = []
    for comment in submission.comments.list():
        if comment.author != 'imtherealcs40bot':
            not_my_comments.append(comment)

    print('Number of Not My Comments: ', len(not_my_comments))

    # Task 2 (2 points)
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented is True:
        reply = generate_comment()
        submission.reply(reply)

    else:

        # Task 3 (2 points)
        comments_without_my_replies = []
        for comment in not_my_comments:
            if comment.author != 'imtherealcs40bot':
                response = False
                for reply in comment.replies:
                    if str(reply.author) == 'imtherealcs40bot':
                        response = True
                if response is False:
                    comments_without_my_replies.append(comment)
        print('Number of Comments Without My Replies: ', len(comments_without_my_replies))

        # Task 4 (2 points)
        for comments in comments_without_my_replies:
            selection = random.choice(comments_without_my_replies)
            generated_reply = generate_comment()
            try:
                selection.reply(generated_reply)
            except praw.exceptions.RedditAPIException as error:
                if "DELETED_COMMENT" in str(error):
                    print("Comment " + comment.id + " was deleted")
                else:
                    print('Error Found: ', error)

    # Task 5 (2 points)
    randomnumber = random.random()
    allsubmissions = []
    if randomnumber >= 0.5:
        print('Original Submission')
        submission = reddit.submission(url='https://www.reddit.com/r/csci040temp/comments/jmarit/rudy_giuliani_is_my_father_please_everyone_vote/')
        submission.reply(generate_comment())
    if randomnumber < 0.5:
        print('Top Subreddit Submission')
        for submission in reddit.subreddit('csci040temp').top(time_filter='month'):
            allsubmissions.append(submission)
        newsubmission = random.choice(allsubmissions)
        submission = reddit.submission(id=newsubmission)
        print('Submission ID: ', newsubmission)
        print(newsubmission.title)

# This can be put after task 4, but I've decided not to include it within the code for organizational reasons
"""
# Bot writes more than 500 comments: 1 point

    # Upvote any comment mentioning your favorite candidate: 1 point
    for comment in submission.comments.list():
        if 'trump' in comment.body.lower():
            comment.upvote()
            print('Comment Upvoted!')

    # Downvote any comment mentioning the opposition: (Probably) 1 point 人(_ _*)
    for comment in submission.comments.list():
        if 'biden' in comment.body.lower():
            comment.downvote()
            print('Comment Downvoted!')

    for submission in reddit.subreddit('csci040temp'):

        # Upvote any submission mentioning your favorite candidate: 1 point
        if 'trump' in submission.title.lower():
            submission.upvote()
            print('Submission Upvoted!')

        # Downvote any submission mentioning the opposition: (Probably) 1 point 人(_ _*)
        if 'biden' in submission.title.lower():
            submission.downvote()
            print('Submission Downvoted!')

    # Upvoting or downvoting comments based on subjectivity and polarity (2 points)
    for comment in submission.comments.list():
        blob = TextBlob(str(comment.body))
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if 'trump' in comment.body.lower() and polarity > 0.5:
            comment.upvote()
        if 'biden' in comment.body.lower() and polarity > 0.5:
            comment.downvote()
        if 'trump' in comment.body.lower() and subjectivity > 0:
            comment.upvote()
        if 'biden' in comment.body.lower() and subjectivity > 0:
            comment.downvote()
"""


# Creating a subreddit for everyone? Priceless, but I'll settle on 5 points ¯\_(ツ)_/¯