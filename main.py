import os
import telebot

API_KEY = "1933071153:AAGtgkS6j5LI4IkWSe3jPH6k0DeI-cgJ5cc"

COMMANDS = {
    
   "MATH" :{
        'command' : 'math'
    },

    "SEND" :{
        'command' : 'send'
    },

    "HELP":{
        'command': 'help'
    }
}


HELP_MESSAGE  = "This bot can do  anything"
mydebugid = '@xerox_synergy_bot'

# Getting the bot instance
bot = telebot.TeleBot(API_KEY)

#bot.send_message(mydebugid, "Wake")
@bot.message_handler(commands=['helss'])
def helss(msg):
    # Send message to person
    bot.send_message(msg.chat.id, HELP_MESSAGE)


#help   
@bot.message_handler(commands=[COMMANDS['HELP']['command']])
def help(message):
    # Send message to person
    bot.send_message(message.chat.id, HELP_MESSAGE)



#solve math 
@bot.message_handler(commands=[COMMANDS['MATH']['command']])
def math(message):
    # Send message to person
    math  =  message.text.split(" ")[1]
    solution  = eval(math)
    bot.send_message(message.chat.id, solution)

bot.polling()