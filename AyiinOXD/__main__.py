# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
""" Userbot start point """
 
 
import  sys
from  importlib  import  import_module
from  platform  import  python_version
 
from  pytgcalls  import  __version__  as  pytgcalls
from  telethon  import  version
from  teleton . tl . alltlobjects  import  LAYER
 
from  AyiinOXDimport  BOT_TOKEN
from  AyiinOXDimport  BOT_VER  as  ubotversion
from  AyiinOXDimport  BOTLOG_CHATID , LOGS , LOOP , bot
from  AyiinOXD . clients  import  ayiin_userbot_on , multiayiin
from  AyiinOXD . cores . git  import  git
from  AyiinOXD . modules  import  ALL_MODULES
from  AyiinOXD . ayiin  import  AyiinDB , HOSTED_ON , autobot , autopilot , ayiin_version
 
try :
 for  module_name  in  ALL_MODULES :
 imported_module  =  import_module ( f"AyiinOXD.modules. { module_name } " )
 adB  =  AyiinDB ()
 client  =  multiayin ()
 total  =  10  -  client
 git ()
 LOGS . info ( f"Total Clients = { total } Users" )
 LOGS . info ( f"Python Version - { python_version () } " )
 LOGS . info ( f"Telethon Version - { version . __version__ } [Layer: { LAYER } ]" )
 LOGS . info ( f"PyTgCalls Version - { pytgcalls } " )
 LOGS . info ( f"Userbot Version - { ubotversion } •[ { adB . name } ]•" )
 LOGS . info ( f"Ayiin Version - { ayiin_version } •[ { HOSTED_ON } ]•" )
 LOGS . info ( "[✨ ACTIVATED SUCCESSFULLY! ]" )
except ( ConnectionError , KeyboardInterrupt , NotImplementedError , SystemExit ):
 pass
except  BaseException  as  e :
 LOGS . info ( str ( e ), exc_info = True )
 sys . exit ( 1 )
 
 
LOOP . run_until_complete ( ayiin_userbot_on ())
if  not  BOTLOG_CHATID :
 LOOP . run_until_complete ( autopilot ())
if  not  BOT_TOKEN :
 LOOP . run_until_complete ( autobot ())
 
if  len ( sys . argv ) not  in ( 1 , 3 , 4 ):
 bots . disconnect ()
else :
 try :
 bots . run_until_disconnected ()
 except  ConnectionError :
 pass
