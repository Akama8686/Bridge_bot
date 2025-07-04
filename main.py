import asyncio
from config import TELEGRAM_BOT_TOKEN
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

async def start(update, context):
    await update.message.reply_text("Привет! Я бот.")

async def help_command(update, context):
    await update.message.reply_text("Вот список команд: /start, /help")

async def echo(update, context):
    await update.message.reply_text(f"Вы сказали: {update.message.text}")

async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🤖 Бот запущен на Render!")
    await app.run_polling()

if name == 'main':
    asyncio.run(main())