from telegram.ext import Updater, MessageHandler, Filters

TOKEN = '2053383240:AAGj4SsOd9OtB7pchx9Vk9VnkJy87VQMLXg'


def msg(update, context):
    user_id = update.effective_chat.id

    message = update.message.text
    message1, message2 = message.split('+')

    context.bot.send_message(chat_id=user_id, text=(int(message1) + int(message2)))

def help(update, context):


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.all, msg)) # Обработчик событий
    updater.start_polling()

