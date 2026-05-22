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

CONTATTO_SIGNAL_URL = "https://signal.me/#eu/Zqcxm0Jfr8OiY0mZVtA7BxNpcYEQvoInjSRMCARGF2xlWavhNINJ6rpzInZ541rs"
GRUPPO_SIGNAL_URL = "https://signal.group/#CjQKID9tL8cCImVFQwpUkUl0dip-eoy5J_dng0hNceDAI0uGEhBI24Ucgn3aGq9JhPfXyaB_"

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
        [
            InlineKeyboardButton(
                "📶 Gruppo Signal",
                url=GRUPPO_SIGNAL_URL
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
                "✈️ Contatto Telegram",
                url=TELEGRAM_CONTACT_URL
            )
        ],
        [
            InlineKeyboardButton(
                "📶 Contatto Signal",
                url=CONTATTO_SIGNAL_URL
            )
        ],
        [
            InlineKeyboardButton(
                "📶 Gruppo Signal",
                url=GRUPPO_SIGNAL_URL
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

    if query.data == "contacts":

        try:
            await query.edit_message_caption(
                caption=(
                    "📞 CONTATTI UFFICIALI\n"
                    "━━━━━━━━━━━━━━\n\n"
                    "Scegli dove contattarci:\n\n"
                    "✈️ Telegram\n"
                    "Supporto diretto.\n\n"
                    "📶 Contatto Signal\n"
                    "Contatto privato diretto.\n\n"
                    "📶 Gruppo Signal\n"
                    "Accesso al gruppo ufficiale.\n\n"
                    "━━━━━━━━━━━━━━"
                ),
                reply_markup=contacts_keyboard()
            )

        except:

            await query.edit_message_text(
                text=(
                    "📞 CONTATTI UFFICIALI\n"
                    "━━━━━━━━━━━━━━\n\n"
                    "Scegli dove contattarci:\n\n"
                    "✈️ Telegram\n"
                    "📶 Contatto Signal\n"
                    "📶 Gruppo Signal"
                ),
                reply_markup=contacts_keyboard()
            )

    elif query.data == "back":

        caption = (
            "🏪 FAMILY FARM — OFFICIAL BOT\n"
            "━━━━━━━━━━━━━━\n\n"
            "Benvenuto nel menu ufficiale.\n"
            "Scegli una sezione qui sotto:\n\n"
            "🛒 Catalogo\n"
            "Consulta prodotti, info e disponibilità.\n\n"
            "📞 Contatti ufficiali\n"
            "Telegram e Signal.\n\n"
            "👥 Community Telegram\n"
            "Accedi al canale ufficiale.\n\n"
            "📶 Gruppo Signal\n"
            "Accedi al gruppo Signal ufficiale.\n\n"
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
