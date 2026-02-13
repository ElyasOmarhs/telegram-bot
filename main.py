import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

# 1. د ویب سرور برخه (ترڅو رینډر ویده نشي)
app = Flask('')

@app.route('/')
def home():
    return "I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. د ټیلیګرام بوټ برخه
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'سلام {update.effective_user.first_name}! زه فعال یم.')

if __name__ == '__main__':
    # لومړی ویب سرور چالانیږي
    keep_alive()
    
    # دلته خپل د بوټ ټوکن (TOKEN) ولیکئ
    TOKEN = "8532339715:AAHjXxMUhd2W97n7P-0otidDbCt1EzmzQGo"
    
    # بوټ چالانیږي
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("Bot is running...")
    application.run_polling()
