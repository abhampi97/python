from telegram import Update # pyright: ignore[reportMissingImports]
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes # pyright: ignore[reportMissingImports]

TELEGRAM_TOKEN = "8346112259:AAHCskXVCwiOh57eI_MIHexUgvVOlTnp0KM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot 🤖")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()