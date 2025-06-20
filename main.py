import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8161800818:AAG025CULWACfuEz6jApsA5l_8bVgbu6mO8"

codewords = ["скидка", "бонус", "start"]

bonus_links = [
    "https://example.com/bonus1",
    "https://example.com/bonus2",
    "https://example.com/bonus3"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот-продажник. Напиши кодовое слово!")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text in codewords:
        link = random.choice(bonus_links)
        await update.message.reply_text(f"Спасибо, вот ваши бонус материалы: {link}")
    else:
        await update.message.reply_text("Я не понял, повтори кодовое слово.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    app.run_polling()
