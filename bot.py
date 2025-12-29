import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
PAYMENT_LINK = os.getenv("PAYMENT_LINK")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 PAGAR", url=PAYMENT_LINK)],
        [InlineKeyboardButton("✅ JÁ PAGUEI", callback_data="paid")]
    ]

    await update.message.reply_text(
        "Para acessar o conteúdo, faça o pagamento e depois clique em ✅ JÁ PAGUEI.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def paid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.message.reply_text(
        f"✅ Acesso liberado:\n{CHANNEL_LINK}"
    )

def main():
    if not BOT_TOKEN or not PAYMENT_LINK or not CHANNEL_LINK:
        raise ValueError("Variáveis de ambiente não configuradas corretamente.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(paid, pattern="^paid$"))
    app.run_polling()

if __name__ == "__main__":
    main()
