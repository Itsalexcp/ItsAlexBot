import os
import sys
import asyncio
import time
import random
import disnake
import defaults
from defaults             import emojis
from defaults             import channels
from defaults             import style
from datetime             import timedelta
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

#Load Commands
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        print(f'Command {filename} wurde geladen!')
        bot.load_extension(f'cmds.{filename[:-3]}')
#Load Client Events
for filename in os.listdir('./events/Client'):
    if filename.endswith('.py'):
        print(f'EventListener {filename} wurde geladen!')
        bot.load_extension(f'events.Client.{filename[:-3]}')
#Load Guild Events
for filename in os.listdir('./events/Guild'):
    if filename.endswith('.py'):
        print(f'EventListener {filename} wurde geladen!')
        bot.load_extension(f'events.Guild.{filename[:-3]}')
#Load Message Events
for filename in os.listdir('./events/Message'):
    if filename.endswith('.py'):
        print(f'EventListener {filename} wurde geladen!')
        bot.load_extension(f'events.message.{filename[:-3]}')

@bot.event
async def on_ready():
    global started
    if not started:
        print("Bot ist online.")
        print("Eingeloggt als Bot {}".format(bot.user.name))
        bot.loop.create_task(status_task())
        print("\nBot ist erfolgreich online gegangen.\n\nLäuft aktuell auf folgenden Server:\n")
        for s in bot.guilds:
            print("  - %s (%s) \nOwner: %s (%s) \nMitglieder: %s Mitglieder \nErstellt am: %s" % (
                s.name, s.id, s.owner, s.owner_id, s.member_count, s.created_at.strftime("%d.%m.%Y, %H:%M Uhr")))
        started = True
        embed = defaults.style.status_on_embed
        await bot.get_channel(defaults.channels.status).send(embed=embed)

    else:
        print('Bot ist offline.')
        embed = defaults.style.status_off_embed
        await bot.get_channel(defaults.channels.status).send(embed=embed)
    return

#Presence
async def status_task():
    while True:
        await bot.change_presence(activity=disnake.Game("ItsAlex Enterprise"),
                                  status=disnake.Status.online)
        await asyncio.sleep(30)
        await bot.change_presence(activity=disnake.Game("Mit Gamerking"),
                                  status=disnake.Status.online)
        await asyncio.sleep(30)
        await bot.change_presence(activity=disnake.Game("Mit ItsAlex"),
                                    status=disnake.Status.online)
        await asyncio.sleep(30)


#starke commands

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Bot fährt in 5 Sekunden runter.")
    await asyncio.sleep(5)
    embed = defaults.style.status_off_embed
    await bot.get_channel(defaults.channels.status).send(embed = embed)
    await bot.close()
    sys.exit(0)

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            print(f'{filename} wurde geladen!')
            bot.reload_extension(f'cmds.{filename[:-3]}')
    await ctx.send("Cogs wurden neu geladen.")



@bot.command()
@commands.is_owner()
async def cogslist(ctx):
    x = os.listdir('./cmds')
    y = os.listdir('./events')
    await ctx.send(f"**COMMANDS**\n {x} \n **EVENTLISTENER**\n {y}")

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} wurde geladen.')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} wurde entladen.')

#Error Handling

@bot.slash_command(description="Antwortet mit Welt!")
async def hello(inter):
    await inter.response.send_message(f"Welt {emojis.Typing}")



@bot.slash_command(description="Sendet ein Küsschen an den User")
async def kuss(inter, person: disnake.Member):
    await inter.response.send_message('Hey ' + person.mention + ' Hier ist ein Küsschen von ' + inter.author.mention + ' :kissing_heart:')
started = False


#connect to discord
#run the bot
import ItsAlex
ItsAlexKey = ItsAlex.TOKEN
bot.run(ItsAlexKey)
