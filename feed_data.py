'''types:
0 => Blog
1 => Internship
2 => Contest
3 => Twitter'''

import twint
import pandas as pd


def feed_data():

    c = twint.Config()
    c.Username = "TheGlobalshala"
    c.Store_csv = True
    c.Custom_csv = ["username", "tweet"]
    c.Output = "Globalshala_Twitter.csv"
    c.Limit = 1

    twint.run.Search(c)

    df = pd.read_csv('Globalshala_Twitter.csv', usecols=[
                     'username', 'tweet', 'urls', 'photos'])
    print(df)

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
            'title': df[0][1],
            'description': df[0][2] + df[0][3],
            'url': 'https://twitter.com/TheGlobalshala/status/1264135763526062080'
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
            'title': df[1][1],
            'description': df[1][2] + df[1][3],
            'url': 'https://twitter.com/TheGlobalshala/status/1263763435717660672'
        }
    ]

    return fd


feed_data()
