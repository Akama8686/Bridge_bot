import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ Переменная окружения TELEGRAM_BOT_TOKEN не установлена!")