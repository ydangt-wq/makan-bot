import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# Ответ в стиле Макана
def makan_style_reply(user_text str) - str
    phrases = [
        Брат, жизнь — как сцена, главное не забывай свою роль 🎤,
        Знаешь, иногда грусть — это просто куплет без припева 💭,
        Я чувствую твой вайб, и он звучит как осень под бит 🌧️,
        Пусть весь мир шумит, но ты будь в тишине, где правда 🔥,
        Не бойся быть собой — даже если мир не на той волне 🎶,
    ]
    import random
    return random.choice(phrases)

async def start(update Update, context ContextTypes.DEFAULT_TYPE)
    await update.message.reply_text(Йо! Я — Макан бот. Напиши мне что-нибудь 🎤)

async def reply(update Update, context ContextTypes.DEFAULT_TYPE)
    text = update.message.text
    response = makan_style_reply(text)
    await update.message.reply_text(response)

if __name__ == __main__
    token = os.getenv(8371349555:AAGLhhD-7rEtFaoKI4qEUqHigjnCa6AZMNo)
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler(start, start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print(✅ Makan Bot is running...)
    app.run_polling()