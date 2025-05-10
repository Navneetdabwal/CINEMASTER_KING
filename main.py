import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from scraper import search_google_link

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome to CINEMASTRO Bot!\n\n"
        "Send any movie name and I’ll search Google for a working streamable link.\n"
        "____________________________________\n"
        "👨‍💻 *Bot Developer:* `『𝙉𝘼𝙑𝙉𝙀𝙀𝙏 𝘿𝘼𝘽𝙒𝘼𝙇』`\n"
        "____________________________________",
        parse_mode="Markdown"
    )

async def movie_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie_name = update.message.text
    await update.message.reply_text("🔍 Searching Google for: " + movie_name)

    link = search_google_link(movie_name)

    if not link:
        await update.message.reply_text("❌ No streamable link found on Google.")
        return

    msg = await update.message.reply_text(
        f"🎬 Found Link:\n{link}\n\n⚠️ Auto-fetched from Google.\n⏱️ This message will delete in 1 minute."
    )
    await asyncio.sleep(60)
    try:
        await msg.delete()
    except:
        pass

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, movie_handler))
app.run_polling()
