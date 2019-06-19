# coding: utf-8

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Test")

conversa = (["Oi", "Olá", "Tudo bem", "Eu estou bem"])

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    quest = input("Você: ")
    response = bot.get_response(quest)
    if float(response.confidence) > 0.5:
        print("Bot: ", response)
    else:
    	print("Bot: Eu não sei!")
