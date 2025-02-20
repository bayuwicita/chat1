import telebot
from telebot import types
import openai
openai.api_key = "sk"
api = '5900318794:AAHQzyvEizB9EK2cMKGeOK7eKwjIBX68xwI'
bot = telebot.TeleBot(api)

def rsp(question):
    prmt = "Q: {qst}\nA:".format(qst=question)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prmt,
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text
@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.send_message(message.chat.id, 'use /chat followed by a question or statement to generate a response')
 
@bot.message_handler(commands=['chat', 'ai', 'ask']) 
def echo_message(message):
 msg = message.text
 #print(msg)
 response = rsp(msg)
 #print(response)
 bot.reply_to(message.chat.id, response)
    
 
print('bot start running')
bot.polling()
