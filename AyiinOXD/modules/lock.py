# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# thanks to anishsk

from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights

from AyiinOXDimport CMD_HANDLER as cmd
from AyiinOXDimport CMD_HELP
from AyiinOXD.events import register
from AyiinOXD.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="lock ?(.*)")
@register(pattern=r"^\.mlock ?(.*)", sudo=True)
async def locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = True
        what = "Pesan"
    elif input_str == "media":
        media = True
        what = "Media"
    elif input_str == "sticker":
        sticker = True
        what = "Sticker"
    elif input_str == "gif":
        gif = True
        what = "GIF"
    elif input_str == "game":
        gamee = True
        what = "Game"
    elif input_str == "inline":
        ainline = True
        what = "Inline Bot"
    elif input_str == "poll":
        gpoll = True
        what = "Poll"
    elif input_str == "invite":
        adduser = True
        what = "Invite"
    elif input_str == "pin":
        cpin = True
        what = "Pin"
    elif input_str == "info":
        changeinfo = True
        what = "Info"
    elif input_str == "all":
        msg = True
        media = True
        sticker = True
        gif = True
        gamee = True
        ainline = True
        gpoll = True
        adduser = True
        cpin = True
        changeinfo = True
        what = "Semuanya"
    else:
        if not input_str:
            await eor(event, get_string("lock_1"))
        else:
            await eor(
                event, get_string("lock_2").format(input_str)
            )
        return
    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    me = await event.client.get_me()
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id, banned_rights=lock_rights)
        )
        await eor(
            event, get_string("lock_3").format(me.first_name, what)
        )
    except BaseException as e:
        await eor(event, get_string("error_1").format(e))

        return


@ayiin_cmd(pattern="unlock ?(.*)")
@register(pattern=r"^\.munlock ?(.*)", sudo=True)
async def rem_locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "Pesan"
    elif input_str == "media":
        media = False
        what = "Media"
    elif input_str == "sticker":
        sticker = False
        what = "Sticker"
    elif input_str == "gif":
        gif = False
        what = "GIF"
    elif input_str == "game":
        gamee = False
        what = "Game"
    elif input_str == "inline":
        ainline = False
        what = "Inline"
    elif input_str == "poll":
        gpoll = False
        what = "Poll"
    elif input_str == "invite":
        adduser = False
        what = "Invite"
    elif input_str == "pin":
        cpin = False
        what = "Pin"
    elif input_str == "info":
        changeinfo = False
        what = "Info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "Semuanya"
    else:
        if not input_str:
            await eor(event, get_string("unlock_1"))
        else:
            await eor(
                event, get_string("unlock_2").format(input_str)
            )
        return
    unlock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    me = await event.client.get_me()
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(
                peer=peer_id, banned_rights=unlock_rights
            )
        )
        await eor(
            event, get_string("unlock_3").format(me.first_name, what)
        )
    except BaseException as e:
        await eor(event, get_string("error_1").format(e))

        return


CMD_HELP.update(
    {
        "locks": f"**Plugin : **`locks`\
        \n\n  »  **Perintah :** `{cmd}lock` <all atau Jenis lock>\
        \n  »  **Kegunaan : **Memungkinkan anda Mengunci beberapa jenis pesan dalam obrolan.\
        \n\n  »  **Perintah :** `{cmd}unlock` <all atau Jenis lock>\
        \n  »  **Kegunaan : **Untuk membuka kunci, beberapa jenis pesan dalam obrolan.\
        \n\n  •  **Jenis pesan yang bisa dikunci atau dibuka adalah:**\
        \n  •  `all, msg, media, sticker, gif, game, inline, poll, invite, pin, info`\
        \n\n  •  **Contoh :** `{cmd}lock msg` atau `{cmd}unlock msg`\
    "
    }
)
