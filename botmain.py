from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I am ready to reply!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This function handles the reply logic
    received_text = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"You said: {received_text}")

if __name__ == '__main__':
    application = ApplicationBuilder().token('8711614541:AAE1kYZzaEfwlw8qOrcS6Mff0pwpxaEZgQ8').build()

    # Command /start
    start_handler = CommandHandler('start', start)
    # Message handler to reply to text
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()
