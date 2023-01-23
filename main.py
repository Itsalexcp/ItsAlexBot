import os
import sys
import asyncio
import time
import random
import disnake
import defaults
import pytz
import MySQLdb
from defaults             import emojis
from defaults             import channels
from defaults             import style
from datetime             import timedelta
from datetime             import datetime
from random               import randint
from disnake.activity     import BaseActivity
from disnake.client       import GatewayParams
from disnake.enums        import Status
from disnake.flags        import Intents, MemberCacheFlags
from disnake.i18n         import LocalizationProtocol
from disnake.mentions     import AllowedMentions
from disnake.message      import Message
from disnake.ext          import commands
from disnake.ext.commands import when_mentioned_or
from disnake.ext.commands import CommandNotFound
from disnake.ext.commands import MissingPermissions
from disnake.ext.commands import MissingRequiredArgument
from disnake.ext.commands import BadArgument
from disnake.ext.commands import NotOwner
from disnake.ext.commands import CommandOnCooldown
from disnake.ext.commands import InvokableUserCommand
from disnake import TextInputStyle


#bot instance
class bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop.create_task(status_task())

#commands sync
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

#Bot Instance
bot = commands.Bot(
                   intents=Intents.all(),
                   case_insensitive=False,
                   test_guilds=[673481402448085024],
                   command_prefix=commands.when_mentioned_or('!'),
                   command_sync_flags=command_sync_flags,
                   description="ItsAlex Enterprise - Ein völlig neuer Bot der auf Disnake basiert.",
                   owner_id= 494959967774834694,
                   reload=True,
          )
#Load cmds
for filename in os.listdir('DEV'):
    if filename.endswith('.py'):
        bot.load_extension(f'DEV.{filename[:-3]}')

for filename in os.listdir('./cmds/general'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.general.{filename[:-3]}')

for filename in os.listdir('./cmds/modalcmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.modalcmds.{filename[:-3]}')

#Load Client Events
for filename in os.listdir('./events/Client'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.Client.{filename[:-3]}')

#Load Guild Events
for filename in os.listdir('./events/Guild'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.Guild.{filename[:-3]}')

#Load Message Events
for filename in os.listdir('./events/Message'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.Message.{filename[:-3]}')

for filename in os.listdir('./discordeasy'):
    if filename.endswith('.py'):
        bot.load_extension(f'discordeasy.{filename[:-3]}')


#push to github
bot.run(os.environ.get("TOKEN"))
#test
#import ItsAlex
#bot.run(ItsAlex.TESTTOKEN)