# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinOXD
#
# This file is a part of < https://github.com/AyiinOXD/Ayiin-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinOXD/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinOXD/Ayiin-Userbot>
# t.me/AyiinOXDSupport & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


from time import sleep
from AyiinOXDimport CMD_HANDLER as cmd
from AyiinOXDimport CMD_HELP
from AyiinOXD.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="cacad(?: |$)(.*)")
async def _(x):
    yins = await eor(x, get_string("yins_47"))
    sleep(2)
    await yins.edit(get_string("yins_48"))
    sleep(1)
    await yins.edit(get_string("yins_49"))
    sleep(2)
    await yins.edit(get_string("yins_50"))


@ayiin_cmd(pattern="hayo(?: |$)(.*)")
async def _(d):
    ayiin = await eor(d, get_string("yins_51"))
    sleep(1)
    await ayiin.edit(get_string("yins_52"))
    sleep(1)
    await ayiin.edit(get_string("yins_53"))
    sleep(1)
    await ayiin.edit(get_string("yins_54"))
    sleep(3)
    await ayiin.edit(get_string("yins_55"))
    sleep(2)
    await ayiin.edit(get_string("yins_56"))
    sleep(2)
    await ayiin.edit(get_string("yins_57"))
    sleep(2)
    await ayiin.edit(get_string("yins_58"))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsubot6": f"**Plugin : **`yinsubot6`\
        \n\n  »  **Perintah :** `{cmd}cacad`\
        \n  »  **Kegunaan :** Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}hayolo`\
        \n  »  **Kegunaan :** Coba Senditi Tod.\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
