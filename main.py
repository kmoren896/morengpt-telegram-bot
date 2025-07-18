
from flask import Flask, request
import telegram

TOKEN = "7621115314:AAH-nSNKJmrH5hSIQ5VQ_ZaxgVoLrY0eDCs"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    bot.sendMessage(chat_id=chat_id, text="👋 Hello, MoReN GPT is active and listening!")
    return "ok"

@app.route("/")
def index():
    return "MoReN Telegram Bot is live!"

if __name__ == "__main__":
    app.run(debug=True)
