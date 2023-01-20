import os
import sys
import asyncio
import time
import random
import disnake
import defaults
import pytz
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


import psycopg2

def connect_to_db():
    connection = psycopg2.connect(
        host="ec2-99-80-170-190.eu-west-1.compute.amazonaws.com",
        port="5432",
        user="uxzhqlzyznggcb",
        password="f9a9c5050f0bb1fed4bf57435c25eed1eace7e9ca22696aa66c3d8a9e611e00e",
        database="d52deb924emnv8"
    )
    return connection

def execute_query(query):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
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


# Create the "settings" table
execute_query("""
CREATE TABLE settings (
    id SERIAL PRIMARY KEY,
    key TEXT NOT NULL,
    value TEXT NOT NULL
)
""")

# Insert some initial data into the table
execute_query("""
INSERT INTO settings (key, value) VALUES
    ('greeting', 'Hello, welcome to my Discord bot!'),
    ('bot_prefix', '!'),
    ('auto_delete_commands', 'true')
""")

# Query the "settings" table to retrieve the value of a specific setting
def get_setting(key):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT value FROM settings WHERE key = %s", (key,))
    setting = cursor.fetchone()
    cursor.close()
    connection.close()
    return setting

# Example usage
greeting = get_setting('greeting')
print(greeting) # Output: "Hello, welcome to my Discord bot!"

#push to github
bot.run(os.environ.get("TOKEN"))
#test
#import ItsAlex
#bot.run(ItsAlex.TESTTOKEN)