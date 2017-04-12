def handle_answer(my_bot, message):
    answer = message.text
    my_bot.reply_to(message, answer)
