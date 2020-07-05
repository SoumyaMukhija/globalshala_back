'''types:
0 => Blog
1 => Internship
2 => Contest
3 => Twitter'''

import twint
import pandas as pd
from random import randrange

def get_random_tweet():
    df = pd.read_csv('predictions/Globalshala_Twitter.csv')
    tweet_data = df.iloc[randrange(len(df))]
    tweet = tweet_data[['tweet', 'link', 'name']]
    return tweet

def feed_data():
    
    tweets = list()
    for i in range(3):
        tweets.append(get_random_tweet())

    fd = [
        {
            'type of content': 0,
            'title': 'MythBuster: Higher Education Courses last three years',
            'description': 'An informative article by Luvpreet Singh',
            'url': 'https://globalshala.com/globalshala_blog/mythbuster-higher-education-courses-last-three-years/'
        },

        {
            'type of content': 1,
            'title': 'Social Media Manager Internship',
            'description': 'You will be responsible for planning social media calendars, creating social media posts, and assisting the social media team with brainstorming campaigns.',
            'url': 'https://globalshala.com/global_iwantto/social-media-manager/'
        },

        {
            'type of content': 2,
            'title': 'Capture with Globalshala',
            'description': 'Can you capture a moment?',
            'url': 'https://globalshala.com/globalshala_contest/capture-with-globalshala/'
        },

        {
            'type of content': 3,
            'title': tweets[0]['tweet'],
            'description': "@"+tweets[0]['name'],
            'url': tweets[0]['link']
        },

        {
            'type of content': 0,
            'title': 'Why setting up HR should be your priority',
            'description': 'An informative article by Harminder Singh.',
            'url': 'https://globalshala.com/globalshala_blog/why-setting-up-hr-should-be-your-priority/'
        },

        {
            'type of content': 1,
            'title': 'Content Writing Internship',
            'description': 'You will be responsible for the ideation and creation of compelling content including blog posts, social media content, and service descriptions.',
            'url': 'https://globalshala.com/global_iwantto/content-writer/'
        },

        {
            'type of content': 2,
            'title': 'Code with Globalshala',
            'description': 'Who is the best code artist?',
            'url': 'https://globalshala.com/globalshala_contest/code-with-globalshala/'
        },

        {
            'type of content': 3,
            'title': tweets[1]['tweet'],
            'description': "@"+tweets[0]['name'],
            'url': tweets[1]['link']
        }
    ]

    return fd


get_random_tweet()
