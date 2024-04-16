import logging
import re

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresiones regulares y respuestas correspondientes
expresiones_respuestas = {
    r"hello|hi|hey|hola": "¡Hola! ¿Cómo estás?",
    r"Buen dia": "Buenas buenas",
    r"Cual es el meta actual?": "Yo soy el meta",
    r"Quien eres?": "Colette",
    r"Cual es tu brawler favorito?": "Tu eres mi brawler favorito JAJAJAJJAJ",
    r"Que piensas de spike?": "No dejo de pensar en él nunca, de hecho, tengo una de sus espinas, conseguirla fue doloroso JAJAJAJAJA",
    r"Que piensas de Crow?": "Sus plumas son excelentes para rellenar almohadas!",
    r"Tu y edgar son?": "Amigos cercanos :3",
    r"-?\d+": "Has ingresado un número entero positivo o negativo.",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages."""
    message_text = update.message.text
    for expresion, respuesta in expresiones_respuestas.items():
        if re.search(expresion, message_text, re.IGNORECASE):
            await update.message.reply_text(respuesta)
            return
    await update.message.reply_text("No entendí tu mensaje.")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token("6403821560:AAFZc42I7UYZsHBVMjkTOI5t8-eyJDbub5A").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
