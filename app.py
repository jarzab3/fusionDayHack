from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pygame

app = Flask(__name__)

bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

bot.set_trainer(ListTrainer)

# Init music
#pygame.init()

#pygame.mixer.music.load("demo.mp3")

# Train the chat bot with a few responses
bot.train([
    'I am not feeling well',
    "I'm here to help you.\nCan you tell me a little more about the issue?",
    'I have a headache',
    'I understand that this is hard for you. \n How are you feeling emotionally?',
    'I am not coping',
    'Can I play you some of your favourite music through Spotify?\nSometimes music helps',
    'Would be great',
    'Do you feel any better?',
    'No',
    'A counsellor will contact you within the next 5 minutes',
    'Thanks',
])

a= [
    "I am not feeling well"
    "I have a headache"
    "I am not coping"
    "Would be great"
    "No"
    "Thanks"
]

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/chat")
def chatbot():
    return render_template("chat.html")

@app.route("/support")
def support():
    return render_template("face.html")

@app.route("/packing")
def packing():
    return render_template("packing-list.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    response = str(bot.get_response(userText))

    if "would be" in userText.lower():
        #pygame.mixer.music.play()
        print("Playing music")
    return response

if __name__ == "__main__":
    app.run(debug=False, port=5000)
