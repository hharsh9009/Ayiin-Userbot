from time import sleep

from AyiinOXDimport CMD_HANDLER as cmd
from AyiinOXDimport CMD_HELP
from AyiinOXD.ayiin import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Assalamualaikum Dulu Biar Sopan**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@ayiin_cmd(pattern="pe(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Assalamualaikum Warahmatullahi Wabarakatuh**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@ayiin_cmd(pattern="P(?: |$)(.*)")
async def _(event):
    me = await event.client.get_me()
    xx = await edit_or_reply(event, f"**Haii Salken Saya {me.first_name}**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@ayiin_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Wa'alaikumsalam**", reply_to=event.reply_to_msg_id
    )
    await event.delete()


@ayiin_cmd(pattern="a(?: |$)(.*)")
async def _(event):
    me = await event.client.get_me()
    xx = await edit_or_reply(event, f"**Haii Salken Saya {me.first_name}**")
    sleep(2)
    await xx.edit("**Assalamualaikum**")


@ayiin_cmd(pattern="j(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await xx.edit("**NIMBRUNG GOBLOKK!!!๐ฅ**")


@ayiin_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    me = await event.client.get_me()
    xx = await edit_or_reply(event, f"**Hallo KIMAAKK SAYA {me.first_name}**")
    sleep(2)
    await xx.edit("**LU SEMUA NGENTOT ๐ฅ**")


@ayiin_cmd(pattern="ass(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**Salam Dulu Biar Sopan**")
    sleep(2)
    await xx.edit("**ุงูุณูููุงููู ุนููููููููู ููุฑูุญูููุฉู ุงูููู ููุจูุฑูููุงุชููู**")


CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  ยป  **Perintah :** `{cmd}p`\
        \n  ยป  **Kegunaan : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  ยป  **Perintah :** `{cmd}pe`\
        \n  ยป  **Kegunaan : **salam Kenal dan salam\
        \n\n  ยป  **Perintah :** `{cmd}l`\
        \n  ยป  **Kegunaan : **Untuk Menjawab salam\
        \n\n  ยป  **Perintah :** `{cmd}ass`\
        \n  ยป  **Kegunaan : **Salam Bahas arab\
        \n\n  ยป  **Perintah :** `{cmd}semangat`\
        \n  ยป  **Kegunaan : **Memberikan Semangat.\
        \n\n  ยป  **Perintah :** `{cmd}ywc`\
        \n  ยป  **Kegunaan : **Menampilkan Sama sama\
        \n\n  ยป  **Perintah :** `{cmd}sayang`\
        \n  ยป  **Kegunaan : **Kata I Love You.\
        \n\n  ยป  **Perintah :** `{cmd}k`\
        \n  ยป  **Kegunaan : **LU SEMUA NGENTOT ๐ฅ\
        \n\n  ยป  **Perintah :** `{cmd}j`\
        \n  ยป  **Kegunaan : **NIMBRUNG GOBLOKK!!!๐ฅ\
    "
    }
)
