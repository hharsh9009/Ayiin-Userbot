import asyncio
from secrets import choice
from time import sleep

from AyiinOXDimport CMD_HANDLER as cmd
from AyiinOXDimport CMD_HELP
from AyiinOXD.events import register as own_cmd
from AyiinOXD.modules.yinsping import absen
from AyiinOXD.ayiin import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="bulan$")
async def _(event):
    event = await edit_or_reply(event, "bulan.")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("bulan..")
    animation_chars = [
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


@ayiin_cmd(pattern="sayang$")
async def _(event):
    e = await edit_or_reply(event, "I LOVEE YOUUU ð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("SAYANG KAMU ððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELAMANYA ð")
    await e.edit("ðððð")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("SAYANG KAMUð")


@ayiin_cmd(pattern=r"dino(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`DIN DINNN.....`")
    sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    sleep(1)
    await typew.edit("`ð                        ð¦`")
    await typew.edit("`ð                       ð¦`")
    await typew.edit("`ð                      ð¦`")
    await typew.edit("`ð                     ð¦`")
    await typew.edit("`ð   `LARII`          ð¦`")
    await typew.edit("`ð                   ð¦`")
    await typew.edit("`ð                  ð¦`")
    await typew.edit("`ð                 ð¦`")
    await typew.edit("`ð                ð¦`")
    await typew.edit("`ð               ð¦`")
    await typew.edit("`ð              ð¦`")
    await typew.edit("`ð             ð¦`")
    await typew.edit("`ð            ð¦`")
    await typew.edit("`ð           ð¦`")
    await typew.edit("`ðWOARGH!   ð¦`")
    await typew.edit("`ð           ð¦`")
    await typew.edit("`ð            ð¦`")
    await typew.edit("`ð             ð¦`")
    await typew.edit("`ð              ð¦`")
    await typew.edit("`ð               ð¦`")
    await typew.edit("`ð                ð¦`")
    await typew.edit("`ð                 ð¦`")
    await typew.edit("`ð                  ð¦`")
    await typew.edit("`ð                   ð¦`")
    await typew.edit("`ð                    ð¦`")
    await typew.edit("`ð                     ð¦`")
    await typew.edit("`ð  Huh-Huh           ð¦`")
    await typew.edit("`ð                   ð¦`")
    await typew.edit("`ð                  ð¦`")
    await typew.edit("`ð                 ð¦`")
    await typew.edit("`ð                ð¦`")
    await typew.edit("`ð               ð¦`")
    await typew.edit("`ð              ð¦`")
    await typew.edit("`ð             ð¦`")
    await typew.edit("`ð            ð¦`")
    await typew.edit("`ð           ð¦`")
    await typew.edit("`ð          ð¦`")
    await typew.edit("`ð         ð¦`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    sleep(1)
    await typew.edit("`ð       ð¦`")
    await typew.edit("`ð      ð¦`")
    await typew.edit("`ð     ð¦`")
    await typew.edit("`ð    ð¦`")
    await typew.edit("`Dahlah Pasrah Aja`")
    sleep(1)
    await typew.edit("`ð§ð¦`")
    sleep(2)
    await typew.edit("`-TAMAT-`")


@ayiin_cmd(pattern="gabut$")
async def _(event):
    e = await edit_or_reply(event, "`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
    await e.edit("`SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA`")
    await e.edit("`RAMBUUUT WARNAAA WARNII`")
    await e.edit("`BAGAI GULALI`")
    await e.edit("`IMUUUTTTTT LUCUUU`")
    await e.edit("`WALAAUUUU TAK TERLALU TINGGI`")
    await e.edit("`GW GABUUTTTT`")
    await e.edit("`EMMMM BACOTNYA`")
    await e.edit("`GABUTTTT WOI GABUT`")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("`CILUUUKKK BAAAAA`")
    await e.edit("ðððð")
    await e.edit("ð¢                       ð¶")
    await e.edit("ð¢                      ð¶")
    await e.edit("ð¢                     ð¶")
    await e.edit("ð¢                    ð¶")
    await e.edit("ð¢                   ð¶")
    await e.edit("ð¢                  ð¶")
    await e.edit("ð¢                 ð¶")
    await e.edit("ð¢                ð¶")
    await e.edit("ð¢               ð¶")
    await e.edit("ð¢              ð¶")
    await e.edit("ð¢             ð¶")
    await e.edit("ð¢            ð¶")
    await e.edit("ð¢           ð¶")
    await e.edit("ð¢          ð¶")
    await e.edit("ð¢         ð¶")
    await e.edit("ð¢        ð¶")
    await e.edit("ð¢       ð¶")
    await e.edit("ð¢      ð¶")
    await e.edit("ð¢     ð¶")
    await e.edit("ð¢    ð¶")
    await e.edit("ð¢   ð¶")
    await e.edit("ð¢  ð¶")
    await e.edit("ð¢ ð¶")
    await e.edit("ð¢ð¶")
    await e.edit("ð¶ð¢")
    await e.edit("ð¶ ð¢")
    await e.edit("ð¶  ð¢")
    await e.edit("ð¶   ð¢")
    await e.edit("ð¶    ð¢")
    await e.edit("ð¶     ð¢")
    await e.edit("ð¶      ð¢")
    await e.edit("ð¶       ð¢")
    await e.edit("ð¶        ð¢")
    await e.edit("ð¶         ð¢")
    await e.edit("ð¶          ð¢")
    await e.edit("ð¶           ð¢")
    await e.edit("ð¶            ð¢")
    await e.edit("ð¶             ð¢")
    await e.edit("ð¶              ð¢")
    await e.edit("ð¶               ð¢")
    await e.edit("ð¶                ð¢")
    await e.edit("ð¶                 ð¢")
    await e.edit("ð¶                  ð¢")
    await e.edit("ð¶                   ð¢")
    await e.edit("ð¶                    ð¢")
    await e.edit("ð¶                     ð¢")
    await e.edit("ð¶                      ð¢")
    await e.edit("ð¶                       ð¢")
    await e.edit("ð¶                        ð¢")
    await e.edit("ð¶                         ð¢")
    await e.edit("ð¶                          ð¢")
    await e.edit("ð¶                           ð¢")
    await e.edit("ð¶                            ð¢")
    await e.edit("ð¶                             ð¢")
    await e.edit("ð¶                              ð¢")
    await e.edit("ð¶                               ð¢")
    await e.edit("ð¶                                ð¢")
    await e.edit("ð¶                                 ð¢")
    await e.edit("`AHHH MANTAP`")
    await e.edit("ð")
    await e.edit("ð")
    await e.edit("ð")
    await e.edit("ð")
    await e.edit("ð")
    await e.edit("ð")
    await e.edit("ð¢                       ð¶")
    await e.edit("ð¢                      ð¶")
    await e.edit("ð¢                     ð¶")
    await e.edit("ð¢                    ð¶")
    await e.edit("ð¢                   ð¶")
    await e.edit("ð¢                  ð¶")
    await e.edit("ð¢                 ð¶")
    await e.edit("ð¢                ð¶")
    await e.edit("ð¢               ð¶")
    await e.edit("ð¢              ð¶")
    await e.edit("ð¢             ð¶")
    await e.edit("ð¢            ð¶")
    await e.edit("ð¢           ð¶")
    await e.edit("ð¢          ð¶")
    await e.edit("ð¢         ð¶")
    await e.edit("ð¢        ð¶")
    await e.edit("ð¢       ð¶")
    await e.edit("ð¢      ð¶")
    await e.edit("ð¢     ð¶")
    await e.edit("ð¢    ð¶")
    await e.edit("ð¢   ð¶")
    await e.edit("ð¢  ð¶")
    await e.edit("ð¢ ð¶")
    await e.edit("ð¢ð¶")
    await e.edit("ð¶ð¢")
    await e.edit("ð¶ ð¢")
    await e.edit("ð¶  ð¢")
    await e.edit("ð¶   ð¢")
    await e.edit("ð¶    ð¢")
    await e.edit("ð¶     ð¢")
    await e.edit("ð¶      ð¢")
    await e.edit("ð¶       ð¢")
    await e.edit("ð¶        ð¢")
    await e.edit("ð¶         ð¢")
    await e.edit("ð¶          ð¢")
    await e.edit("ð¶           ð¢")
    await e.edit("ð¶            ð¢")
    await e.edit("ð¶             ð¢")
    await e.edit("ð¶              ð¢")
    await e.edit("ð¶               ð¢")
    await e.edit("ð¶                ð¢")
    await e.edit("ð¶                 ð¢")
    await e.edit("ð¶                  ð¢")
    await e.edit("ð¶                   ð¢")
    await e.edit("ð¶                    ð¢")
    await e.edit("ð¶                     ð¢")
    await e.edit("ð¶                      ð¢")
    await e.edit("ð¶                       ð¢")
    await e.edit("ð¶                        ð¢")
    await e.edit("ð¶                         ð¢")
    await e.edit("ð¶                          ð¢")
    await e.edit("ð¶                           ð¢")
    await e.edit("ð¶                            ð¢")
    await e.edit("ð¶                             ð¢")
    await e.edit("ð¶                              ð¢")
    await e.edit("ð¶                               ð¢")
    await e.edit("ð¶                                ð¢")
    await e.edit("ð¢                       ð¶")
    await e.edit("ð¢                      ð¶")
    await e.edit("ð¢                     ð¶")
    await e.edit("ð¢                    ð¶")
    await e.edit("ð¢                   ð¶")
    await e.edit("ð¢                  ð¶")
    await e.edit("ð¢                 ð¶")
    await e.edit("ð¢                ð¶")
    await e.edit("ð¢               ð¶")
    await e.edit("ð¢              ð¶")
    await e.edit("ð¢             ð¶")
    await e.edit("ð¢            ð¶")
    await e.edit("ð¢           ð¶")
    await e.edit("ð¢          ð¶")
    await e.edit("ð¢         ð¶")
    await e.edit("ð¢        ð¶")
    await e.edit("ð¢       ð¶")
    await e.edit("ð¢      ð¶")
    await e.edit("ð¢     ð¶")
    await e.edit("ð¢    ð¶")
    await e.edit("ð¢   ð¶")
    await e.edit("ð¢  ð¶")
    await e.edit("ð¢ ð¶")
    await e.edit("ð¢ð¶")
    await e.edit("ð¶ð¢")
    await e.edit("ð¶ ð¢")
    await e.edit("ð¶  ð¢")
    await e.edit("ð¶   ð¢")
    await e.edit("ð¶    ð¢")
    await e.edit("ð¶     ð¢")
    await e.edit("ð¶      ð¢")
    await e.edit("ð¶       ð¢")
    await e.edit("ð¶        ð¢")
    await e.edit("ð¶         ð¢")
    await e.edit("ð¶          ð¢")
    await e.edit("ð¶           ð¢")
    await e.edit("ð¶            ð¢")
    await e.edit("ð¶             ð¢")
    await e.edit("ð¶              ð¢")
    await e.edit("ð¶               ð¢")
    await e.edit("ð¶                ð¢")
    await e.edit("ð¶                 ð¢")
    await e.edit("ð¶                  ð¢")
    await e.edit("ð¶                   ð¢")
    await e.edit("ð¶                    ð¢")
    await e.edit("ð¶                     ð¢")
    await e.edit("ð¶                      ð¢")
    await e.edit("ð¶                       ð¢")
    await e.edit("ð¶                        ð¢")
    await e.edit("ð¶                         ð¢")
    await e.edit("ð¶                          ð¢")
    await e.edit("ð¶                           ð¢")
    await e.edit("ð¶                            ð¢")
    await e.edit("ð¶                             ð¢")
    await e.edit("ð¶                              ð¢")
    await e.edit("ð¶                               ð¢")
    await e.edit("ð¶                                ð¢")
    await e.edit("ð¢                       ð¶")
    await e.edit("ð¢                      ð¶")
    await e.edit("ð¢                     ð¶")
    await e.edit("ð¢                    ð¶")
    await e.edit("ð¢                   ð¶")
    await e.edit("ð¢                  ð¶")
    await e.edit("ð¢                 ð¶")
    await e.edit("ð¢                ð¶")
    await e.edit("ð¢               ð¶")
    await e.edit("ð¢              ð¶")
    await e.edit("ð¢             ð¶")
    await e.edit("ð¢            ð¶")
    await e.edit("ð¢           ð¶")
    await e.edit("ð¢          ð¶")
    await e.edit("ð¢         ð¶")
    await e.edit("ð¢        ð¶")
    await e.edit("ð¢       ð¶")
    await e.edit("ð¢      ð¶")
    await e.edit("ð¢     ð¶")
    await e.edit("ð¢    ð¶")
    await e.edit("ð¢   ð¶")
    await e.edit("ð¢  ð¶")
    await e.edit("ð¢ ð¶")
    await e.edit("ð¢ð¶")
    await e.edit("ð¶ð¢")
    await e.edit("ð¶ ð¢")
    await e.edit("ð¶  ð¢")
    await e.edit("ð¶   ð¢")
    await e.edit("ð¶    ð¢")
    await e.edit("ð¶     ð¢")
    await e.edit("ð¶      ð¢")
    await e.edit("ð¶       ð¢")
    await e.edit("ð¶        ð¢")
    await e.edit("ð¶         ð¢")
    await e.edit("ð¶          ð¢")
    await e.edit("ð¶           ð¢")
    await e.edit("ð¶            ð¢")
    await e.edit("ð¶             ð¢")
    await e.edit("ð¶              ð¢")
    await e.edit("ð¶               ð¢")
    await e.edit("ð¶                ð¢")
    await e.edit("ð¶                 ð¢")
    await e.edit("ð¶                  ð¢")
    await e.edit("ð¶                   ð¢")
    await e.edit("ð¶                    ð¢")
    await e.edit("ð¶                     ð¢")
    await e.edit("ð¶                      ð¢")
    await e.edit("ð¶                       ð¢")
    await e.edit("ð¶                        ð¢")
    await e.edit("ð¶                         ð¢")
    await e.edit("ð¶                          ð¢")
    await e.edit("ð¶                           ð¢")
    await e.edit("ð¶                            ð¢")
    await e.edit("ð¶                             ð¢")
    await e.edit("ð¶                              ð¢")
    await e.edit("ð¶                               ð¢")
    await e.edit("ð¶                                ð¢")
    await e.edit("`GABUT`")


@ayiin_cmd(pattern=r"terkadang(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`Terkadang`")
    sleep(1)
    await typew.edit("`Mencintai Seseorang`")
    sleep(1)
    await typew.edit("`Hanya Akan Membuang Waktumu`")
    sleep(1)
    await typew.edit("`Ketika Waktumu Habis`")
    sleep(1)
    await typew.edit("`Tambah Aja 5000`")
    sleep(1)
    await typew.edit("`Bercanda`")


# Create by myself @localheart


@ayiin_cmd(pattern=r"mf$")
async def _(event):
    await edit_or_reply(event, "`mf g dl` **ã(ã;_ _)ã=3** ")


@ayiin_cmd(pattern=r"(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "cinta":
        await event.edit(input_str)
        animation_chars = [
            "`Connecting Ke Server Cinta`",
            "`Mencari Target Cinta`",
            "`Mengirim Cintaku.. 0%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 4%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 8%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 20%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 36%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 52%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 84%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 100%\nâââââââââCINTAKUâââââââââââ `",
            "`Cintaku Sekarang Sepenuhnya Terkirim Padamu, Dan Sekarang Aku Sangat Mencintai Mu, I Love You ð`",
        ]
        animation_interval = 2
        animation_ttl = range(11)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@ayiin_cmd(pattern=r"gombal(?: |$)(.*)")
async def _(event):
    typew = edit_or_reply(event, "`Hai, I LOVE YOU ð`")
    sleep(1)
    await typew.edit("`I LOVE YOU SO MUCH!`")
    sleep(1)
    await typew.edit("`I NEED YOU!`")
    sleep(1)
    await typew.edit("`I WANT TO BE YOUR BOYFRIEND!`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUðð`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUðð`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUðð`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUðð`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUðð`")
    sleep(1)
    await typew.edit("`Tapi Bo'ong`")


# Create by myself @localheart


@ayiin_cmd(pattern="helikopter(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "â¬â¬â¬.â.â¬â¬â¬ \n"
        "ââââââââ \n"
        "â¢â¤ ââââââââââââ¢â¤ \n"
        "ââ â ââ âââââââââââ¬ \n"
        "â¥ââââââ¤ \n"
        "âââ©âââ©ââ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ Hallo Semuanya :) \n"
        "â¬ââ¬â»/ \n"
        "â¬ââ¬/â \n"
        "â¬ââ¬/ \\ \n",
    )


@ayiin_cmd(pattern="tembak(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "_/ï¹\\_\n" "(Ò`_Â´)\n" "<,ï¸»â¦â¤â Ò\n" r"_/ï¹\_" "\n**Mau Jadi Pacarku Gak?!**",
    )


@ayiin_cmd(pattern="bundir(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "`Dadah Semuanya...`          \nããããã|"
        "\nããããã| \n"
        "ããããã| \n"
        "ããããã| \n"
        "ããããã| \n"
        "ããããã| \n"
        "ããããã| \n"
        "ããããã| \n"
        "ãï¼ï¿£ï¿£ï¼¼| \n"
        "ï¼ Â´ï½¥ ãã |ï¼¼ \n"
        "ã|ãï¼ã | ä¸¶ï¼¼ \n"
        "ï¼ ãï½¥ãã|ããï¼¼ \n"
        "ãï¼¼ï¼¿ï¼¿ï¼âª _ âª) \n"
        "ããããã ï¼µ ï¼µ\n",
    )


@ayiin_cmd(pattern="awk(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "âââââââââââââââââ\n"
        "âââââââââââââââââââ\n"
        "ââââââââââââââââââ\n"
        "ââââââââââââââââââââ\n"
        "ââââââââââââââââââââââ\n`Awkwokwokwok..`",
    )


@ayiin_cmd(pattern="ular(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "âââââ\n"
        "âââââ\n"
        "ââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "ââââââââ\n"
        "ââââââââ\n"
        "ââââââââ\n"
        "ââââââââ\n"
        "ââââââââ\n"
        "ââââââââââ\n"
        "ââââââââââââ\n"
        "ââââââââââââââ\n"
        "ââââââââââââââââ\n"
        "ââââââââââââââââââ\n"
        "âââââââââââââââââââ\n"
        "ââââââââââââââââââââ\n"
        "ââââââââââââââââââââ\n"
        "ââââââââââââââââââââ\n"
        "ââââââââââââââââââââ\n"
        "âââââââââââââââââââ\n"
        "âââââââââââââââââââ\n"
        "âââââââââââââââââââ\n",
    )


@ayiin_cmd(pattern="y(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡ââââ\n"
        "â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡ââ¡â¡â¡â¡â\n"
        "â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡ââ¡â¡â¡â¡â\n"
        "â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡ââ¡â¡â¡â¡â¡â\n"
        "â¡â¡â¡â¡â¡â¡â¡â¡â¡ââ¡â¡â¡â¡â¡â¡â\n"
        "ââââââââââ¡â¡â¡â¡â¡â¡âââââââââ\n"
        "ââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â\n"
        "ââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â\n"
        "ââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â\n"
        "ââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â\n"
        "ââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â\n"
        "ââââââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡ââ\n"
        "ââââââ¡â¡â¡â¡â¡â¡â¡ââââââââââ\n",
    )


@ayiin_cmd(pattern="tank(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "âÛâââââââ]âââââââââââ \n"
        "âââââââââââââââââ¦\n"
        "[âââââââââââââââââââ]\n"
        "â¥ââ²ââ²ââ²ââ²ââ²ââ²ââ¤\n",
    )


@ayiin_cmd(pattern="babi(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "âââââ®â­ââââ­âââââ®\n"
        "âââââââââ­â«Ngok â\n"
        "âââ°âââââ¯â¯â°âââââ¯\n"
        "ââ­ââ»â®â²ââââââ®â­â®â\n"
        "ââââââ²â²â²â²â²â²â£ââ¯â\n"
        "ââ°ââ³â»ââ¯â²â²â²â²ââââ\n"
        "ââââ°ââ³âââ³âââ¯âââ\n"
        "âââââââ»âââ»âââââ\n",
    )


@own_cmd(pattern=r"^\Absendulu$", own=True)
async def _(event):
    await event.reply(choice(absen))


@ayiin_cmd(pattern="ajg(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "â¥âââââââââ­âââ®âââ³\n"
        "â¢â­â®â­ââââââ«ââââââ£\n"
        "â¢ââ°â«ââââââââââ°â«â£\n"
        "â¢â°ââ«ââââââ°â¯â°â³ââ¯â£\n"
        "â¢âââââ³â³âââââ³â«âââ£\n"
        "â¨âââââââââââââââ»\n",
    )


@ayiin_cmd(pattern=r"bernyanyi(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "**Ganteng Doang Gak Bernyanyi (à¸ËoË)à¸§**")
    sleep(2)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")


@ayiin_cmd(pattern="santet(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`Mengaktifkan Perintah Santet Online....`")
    sleep(2)
    await typew.edit("`Mencari Nama Orang Ini...`")
    sleep(1)
    await typew.edit("`Santet Online Segera Dilakukan`")
    sleep(1)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââââ")
    sleep(1)
    await typew.edit("`Target Berhasil Tersantet Online ð¥´`")


CMD_HELP.update(
    {
        "animasi": f"**Plugin :** `animasi`\
        \n\n  Â»  **Perintah : **`{cmd}gabut` | `{cmd}dino`\
        \n  Â»  **Kegunaan :** ntahlah gabut doang.\
        \n\n  Â»  **Perintah : **`{cmd}gombal`\
        \n  Â»  **Kegunaan :** buat bercanda.\
        \n\n  Â»  **Perintah : ** `{cmd}cinta`\
        \n  Â»  **Kegunaan :** mengirim cintamu ke seseorang.\
        \n\n  Â»  **Perintah : **`{cmd}sayang`\
        \n  Â»  **Kegunaan :** untuk jadi buaya.\
        \n\n  Â»  **Perintah : **`{cmd}terkadang`\
        \n  Â»  **Kegunaan :** Auk dah iseng doang.\
        \n\n  Â»  **Perintah : **`{cmd}helikopter` | `{cmd}tank` | `{cmd}tembak` | `{cmd}bundir`\
        \n  Â»  **Kegunaan :** liat sendiri.\
        \n\n  Â»  **Perintah : **`{cmd}y`\
        \n  Â»  **Kegunaan :** jempol\
        \n\n  Â»  **Perintah : **`{cmd}bulan` | `{cmd}hati` | `{cmd}bernyanyi`\
        \n  Â»  **Kegunaan :** liat aja.\
        \n\n  Â»  **Perintah : **`{cmd}awk`\
        \n  Â»  **Kegunaan :** ketawa lari.\
        \n\n  Â»  **Perintah : **`{cmd}lar` | `{cmd}abi` | `{cmd}ajg`\
        \n  Â»  **Kegunaan :** liat sendiri.\
        \n\n  Â»  **Perintah : **`{cmd}bunga` | `{cmd}buah`\
        \n  Â»  **Kegunaan :** animasi.\
        \n\n  Â»  **Perintah : **`{cmd}waktu`\
        \n  Â»  **Kegunaan :** animasi.\
        \n\n  Â»  **Perintah : **`{cmd}santet`\
        \n  Â»  **Kegunaan :** Santet Online Buat Bercanda.\
    "
    }
)
