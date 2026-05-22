import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# =========================================================
# 🔐 TOKEN
# =========================================================

TOKEN = os.getenv("BOT_TOKEN")

# =========================================================
# 🌐 URLS
# =========================================================

LOGO_URL = "https://tgwos.github.io/FAMILY-FARM/LOGOFF.jpg"
CATALOG_URL = "https://tgwos.github.io/FAMILY-FARM/"

TELEGRAM_CONTACT_URL = "https://t.me/familyfarm01"
TELEGRAM_GROUP_URL = "https://t.me/+Z8V2ja92liczMDVk"



# =========================================================
# 🏠 MENU PRINCIPALE
# =========================================================

def main_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🛒 Apri Catalogo",
                web_app=WebAppInfo(url=CATALOG_URL)
            )
        ],
        [
            InlineKeyboardButton(
                "📞 Contatti Ufficiali",
                callback_data="contacts"
            )
        ],
        [
            InlineKeyboardButton(
                "👥 Canale Telegram",
                url=TELEGRAM_GROUP_URL
            )
        ],
    ])

# =========================================================
# 📞 MENU CONTATTI
# =========================================================

def contacts_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "✈️ Telegram",
                url=TELEGRAM_CONTACT_URL
            )
        ],
        [
            InlineKeyboardButton(
                "📶 Signal",
                url=SIGNAL_URL
            )
        ],
        [
            InlineKeyboardButton(
                "📷 Instagram",
                url=INSTAGRAM_URL
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Indietro",
                callback_data="back"
            )
        ]
    ])

# =========================================================
# ▶️ /start
# =========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    caption = (
        "🏪 FAMILY FARM — OFFICIAL BOT\n"
        "━━━━━━━━━━━━━━\n\n"
        "Benvenuto nel menu ufficiale.\n"
        "Scegli una sezione qui sotto:\n\n"
    )

    try:
        await update.message.reply_photo(
            photo=LOGO_URL,
            caption=caption,
            reply_markup=main_keyboard()
        )

    except Exception as e:

        print("❌ Errore caricamento logo:", e)

        await update.message.reply_text(
            text=caption,
            reply_markup=main_keyboard()
        )

# =========================================================
# 🔘 GESTIONE PULSANTI
# =========================================================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # =========================
    # 📞 CONTATTI
    # =========================

    if query.data == "contacts":

        try:
            await query.edit_message_caption(
                caption=(
                    "📞 CONTATTI UFFICIALI\n"
                    "━━━━━━━━━━━━━━\n\n"
                    "Scegli dove contattarci:\n\n"
                    "✈️ Telegram\n"
                    "Supporto diretto.\n\n"
                    "📶 Signal\n"
                    "Canale privato di contatto.\n\n"
                    "📷 Instagram\n"
                    "Profilo ufficiale.\n\n"
                    "━━━━━━━━━━━━━━"
                ),
                reply_markup=contacts_keyboard()
            )

        except:

            await query.edit_message_text(
                text=(
                    "📞 CONTATTI UFFICIALI\n"
                    "━━━━━━━━━━━━━━\n\n"
                    "Scegli dove contattarci:"
                ),
                reply_markup=contacts_keyboard()
            )

    # =========================
    # ⬅️ BACK
    # =========================

    elif query.data == "back":

        caption = (
            "🏪 FAMILY FARM — OFFICIAL BOT\n"
            "━━━━━━━━━━━━━━\n\n"
            "Benvenuto nel menu ufficiale.\n"
            "Scegli una sezione qui sotto:\n\n"
            "🛒 Catalogo\n"
            "Consulta prodotti, info e disponibilità.\n\n"
            "📞 Contatti ufficiali\n"
            "Telegram, Signal e Instagram.\n\n"
            "👥 Community Telegram\n"
            "Accedi al canale ufficiale.\n\n"
            "━━━━━━━━━━━━━━\n"
            "✅ Supporto rapido\n"
            "🔒 Solo canali ufficiali\n"
            "📦 Catalogo sempre aggiornato"
        )

        try:
            await query.edit_message_caption(
                caption=caption,
                reply_markup=main_keyboard()
            )

        except:

            await query.edit_message_text(
                text=caption,
                reply_markup=main_keyboard()
            )

# =========================================================
# 🚀 AVVIO BOT
# =========================================================

def main():

    if not TOKEN:
        raise RuntimeError("❌ BOT_TOKEN non impostato")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("✅ Bot avviato correttamente")

    app.run_polling()

# =========================================================
# ▶️ MAIN
# =========================================================

if __name__ == "__main__":
    main()
