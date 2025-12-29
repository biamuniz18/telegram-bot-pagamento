import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# ===============================
# ENV VARS (Render)
# ===============================
BOT_TOKEN = os.getenv("BOT_TOKEN")
PAYMENT_LINK = os.getenv("PAYMENT_LINK")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")

# ===============================
# COMMAND /start
# ===============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 PAGAR AGORA", url=PAYMENT_LINK)],
        [InlineKeyboardButton("📢 ACESSAR CANAL", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "✅ Bem-vindo!\n\n"
        "Clique abaixo para realizar o pagamento.\n"
        "Após o pagamento, acesse o canal:",
        reply_markup=reply_markup
    )

# ===============================
# MAIN
# ===============================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot iniciado com sucesso...")
    app.run_polling()

if __name__ == "__main__":
    main() 
