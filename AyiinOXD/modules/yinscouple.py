# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinOXD
#
# This file is a part of < https://github.com/AyiinOXD/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinOXD/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinOXD/Ayiin-Userbot>
# t.me/AyiinOXDSupport & t.me/AyiinSupport

from secrets import choice
from telethon.tl.types import InputMessagesFilterPhotos

from AyiinOXDimport CMD_HANDLER as cmd
from AyiinOXDimport CMD_HELP
from AyiinOXD.ayiin import ayiin_cmd, eor
from Stringyins import get_string


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern="couple(?: |$)(.*)")
async def couple(bucin):
    copl = await eor(bucin, get_string("com_1"))
    try:
        bucinan = [
            coupl
            async for coupl in bucin.client.iter_messages(
                "@ppayiinuserbot", filter=InputMessagesFilterPhotos
            )
        ]
        cang = await bucin.client.get_me()
        await bucin.client.send_file(
            bucin.chat_id,
            file=choice(bucinan),
            caption=get_string("yicpl_1"). format(cang.first_name, cang.id)
        )
        await copl.delete()
    except Exception:
        await copl.edit(get_string("yicpl_2"))


CMD_HELP.update(
    {
        "yinscouple": f"**Plugin :** `yinscouple`\
        \n\n  »  **Perintah :** `{cmd}couple`\
        \n  »  **Kegunaan :** __Untuk Mendapatkan Foto Couple Secara Random.__\
    "
    }
)
