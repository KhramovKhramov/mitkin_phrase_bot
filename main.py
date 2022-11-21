import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from bot import settings
from bot.handlers import get_phrase, greet_user, learning

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.regex("^(Вперед)$"), learning))
    dp.add_handler(MessageHandler(Filters.regex("^(вперед)$"), learning))
    dp.add_handler(MessageHandler(Filters.regex("^(Добавить)$"), learning))
    dp.add_handler(MessageHandler(Filters.regex("^(Пропустить)$"),  learning))
    dp.add_handler(MessageHandler(Filters.regex("Митькин"), get_phrase))
    dp.add_handler(MessageHandler(Filters.regex("митькин"), get_phrase))
    dp.add_handler(MessageHandler(Filters.regex("гол"), get_phrase))
    dp.add_handler(MessageHandler(Filters.regex("сайт"), get_phrase))
    dp.add_handler(MessageHandler(Filters.regex("степаныч"), get_phrase))
    dp.add_handler(MessageHandler(Filters.regex("Степаныч"), get_phrase))
    dp.add_handler(MessageHandler(Filters.regex("забил"), get_phrase))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
