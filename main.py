import telebot
from datetime import datetime
from decouple import config


from answer_to_user import handle_answer
from commands_handler import commands_handler, commands


TOKEN = str(config('TOKEN'))
MY_BOT = telebot.TeleBot(TOKEN)


def do_logging(message, answer):
    print('-----------')
    print(datetime.now())
    print("Message from `{0} {1}`.\nText - {2}".format(
        message.from_user.first_name,
        message.from_user.last_name,
        message.text))
    print("Bot's answer: " + answer)


@MY_BOT.message_handler(commands=["ping"])
def on_ping(message):
    MY_BOT.reply_to(message, "Still alive and kicking!")


@MY_BOT.message_handler(commands=commands)
def send_welcome_message(command):
    if command.text[1:] in commands:
        commands_handler(MY_BOT, command)
        do_logging(command, "Sent keyboard with commands")
    else:
        print("Error! No correct command found!")


@MY_BOT.message_handler(content_types=['text'])
def send_arbitrary_message(message):
    if message.text:
        handle_answer(MY_BOT, message)
        do_logging(message, "Sent to the handler function")


MY_BOT.polling(none_stop=True, interval=0)
