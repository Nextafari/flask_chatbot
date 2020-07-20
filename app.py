from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)

# naming the bot
bot = ChatBot("Demo_bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

# chatterbot class for training the bot
#trainer = ChatterBotCorpusTrainer(bot)

trainer = ListTrainer(bot)



trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response")
def get_bot_response():
    userText = request.args.get("msg")
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()