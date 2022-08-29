from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler

button_help = '1 строка'
button_reference = '1.2 строка'
button_db = '1.3 строка'

button_horiz = '2 строка'
button_horiz2 = '2.1 строка'


def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Это ответ на строку 1(меню закрылось)!',
        reply_markup=ReplyKeyboardRemove(),
    )


def button_db_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='это ответ на строку 1.3(меню закрылось)',
        reply_markup=ReplyKeyboardRemove(),
    )


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help:
        return button_help_handler(update=update, context=context)
    if text == button_db:
        return button_db_handler(update=update,context=context)

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help),
                KeyboardButton(text=button_reference),
                KeyboardButton(text=button_db),
            ],
            [
                KeyboardButton(text=button_horiz),
                KeyboardButton(text=button_horiz2)],
            ],
        resize_keyboard=True
    )

    update.message.reply_text(
        text='Ася лох',
        reply_markup=reply_markup,
    )


def main():
    with open('token.txt', 'r') as file:
        token_file = file.read().strip()

    print('Start')
    updater = Updater(
        token=token_file,
        use_context=True,
    )

    print(updater.bot.get_me())

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all,
                                                  callback=message_handler))

    updater.start_polling()
    updater.idle()

    print('Finish')


#
#
if __name__ == '__main__':
    main()
