import os
import sys
import asyncio
import time
import random
import disnake
import defaults
import pytz
import sqlite3
from disnake import TextInputStyle
from defaults             import emojis, channels, style
from datetime             import timedelta, datetime
from random               import randint
from disnake.activity     import BaseActivity
from disnake.client       import GatewayParams
from disnake.enums        import Status
from disnake.flags        import Intents, MemberCacheFlags
from disnake.i18n         import LocalizationProtocol
from disnake.mentions     import AllowedMentions
from disnake.message      import Message
from disnake.ext          import commands
from disnake.ext.commands import when_mentioned_or, CommandNotFound, MissingPermissions, MissingRequiredArgument, BadArgument, NotOwner, CommandOnCooldown, InvokableUserCommand


connection = sqlite3.connect("database.db")
cursor = connection.cursor()



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
def load_cogs():
    for folder, subfolder, file in os.walk("cogs/"):
        for filename in file:
            if filename.endswith(".py"):
                filenamepath = os.path.join(folder, filename)
                filenamepath = filenamepath.replace("\\", ".")
                filenamepath = filenamepath.replace("/", ".")
                filenamepath = filenamepath.replace(".py", "")
                bot.load_extension(filenamepath)

load_cogs()

#push to github
bot.run(os.environ.get("TOKEN"))
#test
#import ItsAlex
#bot.run(ItsAlex.TESTTOKEN)