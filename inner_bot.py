from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from config import TELEGRAM_BOT_TOKEN
from deepseek_api import ask
from utils.session_manager import start_session, next_step, get_mask, has_session


TRACKS = {"Я застрял": "ya_zastryal", "Надо решиться": "nado_reshitsya"}
MASKS = {"Уличный мудрец": "streetwise", "Женский голос": "wise_woman"}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[track] for track in TRACKS]
    await update.message.reply_text(
        "Привет. Выбери тему сессии:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True),
    )
    context.user_data["state"] = "choose_track"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    state = context.user_data.get("state")

    if state == "choose_track" and text in TRACKS:
        context.user_data["track"] = TRACKS[text]
        keyboard = [[mask] for mask in MASKS]
        await update.message.reply_text(
            "Выбери голос наставника:",
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True),
        )
        context.user_data["state"] = "choose_mask"
        return

    if state == "choose_mask" and text in MASKS:
        track = context.user_data["track"]
        mask = MASKS[text]
        first_question = start_session(user_id, track, mask)
        await update.message.reply_text(first_question)
        context.user_data["state"] = "in_session"
        return

    if state == "in_session" and has_session(user_id):
        # Генерируем реакцию наставника на ответ пользователя
        mask_prompt = get_mask(user_id)
        reaction = ask(mask_prompt, text)
        await update.message.reply_text(reaction)

        # Переходим к следующему вопросу трека
        next_question = next_step(user_id)
        if next_question:
            await update.message.reply_text(next_question)
        else:
            await update.message.reply_text(
                "Сессия завершена. Спасибо за честность с собой.\n\nЧтобы начать новую — /start"
            )
            context.user_data["state"] = None
        return

    await update.message.reply_text("Начни сессию: /start")


def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("INNER запущен")
    app.run_polling()


if __name__ == "__main__":
    main()
