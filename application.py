from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
from datetime import date
from datetime import datetime


application = Flask(__name__)

# naming the bot
bot = ChatBot("Demo_bot")
# , storage_adapter="chatterbot.storage.SQLStorageAdapter")

# chatterbot class for training the bot
#trainer = ChatterBotCorpusTrainer(bot)

trainer = ListTrainer(bot)

today = str(date.today())
date_today = ("Today is, " + today)

date_and_time = str(datetime.now())
say_datetime = ("Today's date and time are " + date_and_time)

conversations = [
    "Hello",
    "Hi, how may I help you ?",
    "What is your name ?",
    "My name is Ikenga cos I a deity",
    "Who are you ?",
    "I am Ikenga, I strike thunder"
    "How are you today ?",
    "I am quite well, thank you.",
    "What is today's date ?",
    date_today,
    "What is today ?",
    say_datetime,
    "Are you sapien ?",
    "No I am just a chatbot built by Emmanuel",
    "What do you know ?",
    "I know as much as my Lord lets me know",
    "Are you male or female ?",
    "I am whatever you want me to be",
]


trainer.train(conversations)

# trainer.train("chatterbot.corpus.english")

@application.route("/")
def home():
    return render_template("index.html")

@application.route("/get_response")
def get_bot_response():
    userText = request.args.get("msg")
    return str(bot.get_response(userText))



if __name__ == "__main__":
   application.run(debug=True,host='0.0.0.0')
