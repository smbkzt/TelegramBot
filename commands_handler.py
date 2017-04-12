from telebot import types

commands = ['start', 'help', 'stop']
text_messages = {
    'welcome':
        u'Please welcome {name}!\n'
        u'This chat is intended for questions about and discussion of the pyTelegramBotAPI.\n'
        u'I hope you enjoy your stay here!',

    'info':
        u'My name is Jarvis,\n'
        u'I am a bot that assists these wonderful bot-creating people of this bot library group chat.\n'
        u'Also, I am still under development. Please improve my functionality by making a pull request! '
        u'Suggestions are also welcome, just drop them in this group chat!',

    'wrong_chat':
        u'Hi there!\nThanks for trying me out. However, this bot can only be used in the pyTelegramAPI group chat.\n'
        u'Join us!\n\n'
        u'https://telegram.me/joinchat/067e22c60035523fda8f6025ee87e30b'
}


def commands_handler(my_bot, command):
    if command.text == '/start':
        markup = types.ReplyKeyboardMarkup(True, False)
        markup.row('/start', '/stop')
        my_bot.send_message(command.from_user.id, text_messages['welcome'],
                            reply_markup=markup)
    elif command.text == '/help':
        my_bot.send_message(command.from_user.id, text_messages['info'])
    elif command.text == '/stop':
        hide_markup = types.ReplyKeyboardRemove()
        my_bot.send_message(command.from_user.id,
                            '...', reply_markup=hide_markup)

    else:
        my_bot.send_message(command.from_user.id,
                            'Some error occured! No commands like that')
