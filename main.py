
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 OTC SIGNAL PRO\n\n"
        "Bot conectado correctamente.\n"
        "Escribe /senal para solicitar un análisis.\n\n"
        "Estado: esperando conexión de datos OTC."
    )


async def senal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔎 Solicitud recibida.\n\n"
        "Todavía estamos configurando la fuente "
        "de datos OTC.\n"
        "No se generarán señales sin datos reales."
    )


def main():
    if not TOKEN:
        raise RuntimeError("Falta configurar BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("senal", senal))

    print("OTC SIGNAL PRO iniciado.")
    app.run_polling()


if __name__ == "__main__":
    main()
