from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJRNZgc4GPPxQ9q7CO5m2Ft9htxNuFHwACDwEAAlEpDTmkePNDDnym2x4E")
    await message.reply_text(
        f"""**Haiiiii Gays {bn} 🎵

Saya bisa memutar musik di panggilan suara grup Anda. Dikembangkan Oleh [Vckyyy](https://t.me/VckyouuBitch).

Tambahkan saya ke grup Anda dengan cara salin username saya lalu invite, jangan lupa invite juga @GeezMusicAssitant dan nikmati musik yang kami mulai dengan bebas!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Klik Disini Untuk Penjelasan Printah", url="https://telegra.ph/text-04-11-2")
                  ],[
                    InlineKeyboardButton(
                        "✨ Pemilik", url="https://t.me/VckyouuBitch"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Vckyouuu"
                    )
                 ],[ 
                    InlineKeyboardButton(
                        "Masukan Bot Dan Assistant Ke Grup Anda!",
                         url="t.me/{}?startgroup=true".format(
                                context.bot.username
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
                        "🔊 Channel", url="https://t.me/Vckyouuu")
                ]
            ]
        )
   )


