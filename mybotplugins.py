from slackbot.bot import respond_to
from slackbot.bot import listen_to
import json
import re
import random
import os

#AIzaSyBAlAqrKdsHl_6cLLo0I8t5L1rDQpJb7pQ

@respond_to('hi$', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')


@respond_to('hi$', re.IGNORECASE)
def hi(message):
    message.reply('Hi')
    message.react('+1')
    message.react('+1')

@respond_to('I love you',re.IGNORECASE)
def love(message):
    message.reply('I love you too!')

@listen_to('who is the spy?',re.IGNORECASE)
def newconn(message):
    message.reply('Yes,am the spy. i can read all channel messages and take some screen shot :)')


@listen_to('break*',re.IGNORECASE)
def help(message):
    message.reply("Sure, Lets Move On Dev's Let Drink Cup Of Tea!")
    message.react('+1')
    message.send('Hurray Break !!!!!')


@respond_to('quote',re.IGNORECASE)
def help(message):
    quote_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.txt')
    f = open(quote_file, 'r')
    txt = f.read()
    lines = txt.split('\n.\n')
    message.reply(random.choice(lines))


@listen_to('quote',re.IGNORECASE)
def help(message):
    quote_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.txt')
    f = open(quote_file, 'r')
    txt = f.read()
    lines = txt.split('\n.\n')
    message.reply(random.choice(lines))

@listen_to('lunch*',re.IGNORECASE)
def help(message):
    message.reply("Whats Special Today !")
    message.react('+1')
    message.send('Lets Move')



@listen_to('Can someone help me?')
def help1(message):
    message.reply('Yes, I can!')
    message.send('I can help everybody!')
    message.reply("Here's a threaded reply", in_thread=True)

@respond_to('break*')
def giveme(message):
    message.reply('Here is ')

@respond_to('github', re.IGNORECASE)
def github(message):
    attachments = [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": "#36a64f",
            "pretext": "Optional text that appears above the attachment block",
            "author_name": "Bobby Tables",
            "author_link": "http://flickr.com/bobby/",
            "author_icon": "http://flickr.com/icons/bobby.jpg",
            "title": "Slack API Documentation",
            "title_link": "https://api.slack.com/",
            "text": "Optional text that appears within the attachment",
            "fields": [
                {
                    "title": "Priority",
                    "value": "High",
                    "short": "false"
                }
            ],
            "image_url": "http://my-website.com/path/to/image.jpg",
            "thumb_url": "http://example.com/path/to/thumb.png",
            "footer": "Slack API",
            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
            "ts": 123456789
        }
    ]
    message.send_webapi('', json.dumps(attachments))
