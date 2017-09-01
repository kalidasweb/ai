from slackbot.bot import Bot
import logging

def main():
    bot = Bot()
    logging.basicConfig()
    bot.run()

if __name__ == "__main__":
    main()
