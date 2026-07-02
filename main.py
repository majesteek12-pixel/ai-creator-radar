import os
import logging
import asyncio
from flask import Flask
from threading import Thread
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from app.search import search_opportunities
from app.messages import format_opportunities, welcome_message, help_message
ALLOWED_USER_ID = 297309691
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "AI Creator Radar is running"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port)
load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("⛔ Доступ запрещён")
        return

    await update.message.reply_text(welcome_message(), parse_mode="Markdown")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(help_message(), parse_mode="Markdown")


async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    items = search_opportunities("jobs")
    await update.message.reply_text(format_opportunities("💼 AI-вакансии", items), parse_mode="Markdown", disable_web_page_preview=True)


async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    items = search_opportunities("projects")
    await update.message.reply_text(format_opportunities("💰 Фриланс-проекты", items), parse_mode="Markdown", disable_web_page_preview=True)


async def remote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    items = search_opportunities("remote")
    await update.message.reply_text(format_opportunities("🌍 Remote-возможности", items), parse_mode="Markdown", disable_web_page_preview=True)


async def cartoons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    items = search_opportunities("cartoons")
    await update.message.reply_text(format_opportunities("🎬 Мультфильмы и AI-анимация", items), parse_mode="Markdown", disable_web_page_preview=True)


async def grants(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    items = search_opportunities("grants")
    await update.message.reply_text(format_opportunities("🏆 Гранты и конкурсы", items), parse_mode="Markdown", disable_web_page_preview=True)


async def top(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    items = search_opportunities("top")
    await update.message.reply_text(format_opportunities("🔥 ТОП возможностей дня", items), parse_mode="Markdown", disable_web_page_preview=True)


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set. Add it to .env or Render Environment Variables.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("jobs", jobs))
    app.add_handler(CommandHandler("projects", projects))
    app.add_handler(CommandHandler("remote", remote))
    app.add_handler(CommandHandler("cartoons", cartoons))
    app.add_handler(CommandHandler("grants", grants))
    app.add_handler(CommandHandler("top", top))

    logging.info("AI Creator Radar bot started.")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    Thread(target=run_web, daemon=True).start()
    app.run_polling()


if __name__ == "__main__":
    main()
    
