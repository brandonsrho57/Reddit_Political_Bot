import praw
import random
import datetime

def generate_comment_0():
    joenames = ['Joe', 'Biden', 'Joe Biden', 'Joseph Biden', 'Joey', 'Joseph', 'Joseph Robinette Biden Jr.',"Obama's Vice President"]
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
    donaldnames = ['Donald', 'Trump', 'Donald Trump', 'Donald J. Trump', 'Donald John Trump', 'The President','Businessman Trump', 'Trumpster']
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
    joenames = ['Joe', 'Biden', 'Joe Biden', 'Joseph Biden', 'Joey', 'Joseph', 'Joseph Robinette Biden Jr.',"Obama's Vice President"]
    joebiden = random.choice(joenames)
    donaldnames = ['Donald', 'Trump', 'Donald Trump', 'Donald J. Trump', 'Donald John Trump', 'The President','Businessman Trump', 'Trumpster']
    donaldtrump = random.choice(donaldnames)
    choose = ['vote', 'choose', 'pick', 'select', 'take']
    vote = random.choice(choose)
    jobs = ['blue-collar worker', 'white-collar worker', 'Walmart employee', 'programmer', 'student']
    job = random.choice(jobs)
    office = ['the White House', 'the Oval Office', 'office', 'the house']
    wh = random.choice(office)

    text = "Although both " + joebiden + " and " + donaldtrump + " are decent candidates, I'm inclined to " + vote + " " + joebiden + " because I'm just a " + job + " who just wants things to go back to what they were. If " + donaldtrump + " gets another 4 years in the " + wh + ", I'm afraid of the division."
    return text

#Last 3 will be unsupportive messages
def generate_comment_3():
    joenames = ['Joe', 'Biden', 'Joe Biden', 'Joseph Biden', 'Joey', 'Joseph', 'Joseph Robinette Biden Jr.',"Obama's Vice President"]
    joebiden = random.choice(joenames)
    donaldnames = ['Donald', 'Trump', 'Donald Trump', 'Donald J. Trump', 'Donald John Trump', 'The President','Businessman Trump', 'Trumpster']
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
    joenames = ['Joe', 'Biden', 'Joe Biden', 'Joseph Biden', 'Joey', 'Joseph', 'Joseph Robinette Biden Jr.',"Obama's Vice President"]
    joebiden = random.choice(joenames)
    donaldnames = ['Donald', 'Trump', 'Donald Trump', 'Donald J. Trump', 'Donald John Trump', 'The President','Businessman Trump', 'Trumpster']
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
        options = [0,1,2,3,4,5]
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

reddit = praw.Reddit('i_am_michael_izbicki_bot')
reddit_debate_url = 'https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/'
submission = reddit.submission(url=reddit_debate_url)

while True:
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)
    submission.comments.replace_more(limit=10)

    all_comments = []
    for comment in submission.comments.list():
        all_comments.append(comment)
    print('All Comments: ',all_comments)
    print('len(all_comments)=',len(all_comments))

    not_my_comments = []
    for comment in submission.comments.list():
        if comment.author != 'imtherealcs40bot':
            not_my_comments.append(comment)

    print('Not My Comments',not_my_comments)
    print('len(not_my_comments)=',len(not_my_comments))

    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented is True:
        reply = generate_comment()
        submission.reply(reply)

    else:
        comments_without_my_replies = []
        for comment in not_my_comments:
            if comment.author != 'imtherealcs40bot':
                response = False
                for reply in comment.replies:
                    if str(reply.author) == 'imtherealcs40bot':
                        response = True
                if response is False:
                    comments_without_my_replies.append(comment)
        print('Comments Without My Replies:', comments_without_my_replies)
        print('len(comments_without_replies)=', len(comments_without_my_replies))

        for comments in comments_without_my_replies:
            selection = random.choice(comments_without_my_replies)
            generated_reply = generate_comment()
            try:
                selection.reply(generated_reply)
            except praw.exceptions.RedditAPIException as error:
                if "DELETED_COMMENT" in str(error):
                    print("Comment " + comment.id + " was deleted")
                else:
                    print(error)

    random_submission = reddit.subreddit('csci040').top(time_filter='month').random()
    choices = [random_submission, submission]
    number = random.randint(0, 101)

    if number < 50:
        submission = random_submission
    else:
        submission = reddit.submission(url=reddit_debate_url)