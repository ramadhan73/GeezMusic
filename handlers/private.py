from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJRNZgc4GPPxQ9q7CO5m2Ft9htxNuFHwACDwEAAlEpDTmkePNDDnym2x4E")
    await message.reply_text(
        f"""**Hai Aku. {bn} 🎵

Saya bisa memutar musik di panggilan suara grup Anda. Dikembangkan Oleh [Vckyyy](https://t.me/VckyouuBitch).

Note : Gunakan Bot Ini Dengan Bijak, Jika Terjadi Kendala Silahkan Hubungi [Vckyyy](https://t.me/VckyouuBitch).
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Klik Disini Untuk Penjelasan Printah", url="https://telegra.ph/text-04-11-2")
                  ],[
                    InlineKeyboardButton(
                        "✨ Group", url="https://t.me/LordUserbot_Group"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel Info", url="https://t.me/Vckyouuu"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel Info", url="https://t.me/Vckyouuu")
                ]
            ]
        )
   )


