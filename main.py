import os
import sys
import asyncio
import time
import random
import disnake
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

#bot Instanz erstellen
class bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop.create_task(status_task())

#commands syncen
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

#Bot Instanz
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


#Cogs laden und lesen
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print(f'{filename} wurde geladen!')
        bot.load_extension(f'cogs.{filename[:-3]}')


#GuildTracker
news_channel = 1038885196436611125
guild_tracker_channel = 1040236424978518107
message_tracker_channel = 1040236446306537533
channel_tracker_channel = 1040259496787849246
member_tracker_channel = 1040260095579275304
invite_tracker_channel = 1040364889480372254
role_tracker_channel = 1040364828885266513

default_event_embed = disnake.Embed(
    color = disnake.Colour.yellow(),
    timestamp = disnake.utils.utcnow()
)
default_event_embed.set_author(
    name="Ich habe etwas aufgezeichnet",
    icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
                     "/AppIconGhostStation.png")
default_event_embed.set_footer(
    text="Dies ist ein Service von ItsAlex Enterprise",
)

@bot.event
async def on_guild_update(before: disnake.Guild, after: disnake.Guild):
    if before.name != after.name:
        embed = default_event_embed
        embed.title = "Servername geändert"
        embed.description = f"Der Servername wurde von **{before.name}** zu **{after.name}** geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.premium_tier != after.premium_tier:
        embed = default_event_embed
        embed.title = "Serverboost geändert"
        embed.description = f"Der Serverboost wurde von **{before.premium_tier}** zu **{after.premium_tier}** geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.verification_level != after.verification_level:
        embed = default_event_embed
        embed.title = "Serververifizierung geändert"
        embed.description = f"Die Serververifizierung wurde von **{before.verification_level}** zu **{after.verification_level}** geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.owner_id != after.owner_id:
        embed = default_event_embed
        embed.title = "Serverbesitzer geändert"
        embed.description = f"Der Serverbesitzer wurde von **<@{before.owner_id}>** zu **<@{after.owner_id}>** geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.vanity_url_code != after.vanity_url_code:
        embed = default_event_embed
        embed.title = "Server Vanity geändert"
        embed.description = f"Der Server Vanity wurde von {before.vanity_url_code} zu {after.vanity_url_code} geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.description != after.description:
        embed = default_event_embed
        embed.title = "Serverbeschreibung geändert"
        embed.description = f"Die Serverbeschreibung wurde von **{before.description}** zu **{after.description}** geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.banner != after.banner:
        embed = default_event_embed
        embed.title = "Serverbanner geändert"
        embed.description = f"Der Serverbanner wurde von {before.banner} zu {after.banner} geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.splash != after.splash:
        embed = default_event_embed
        embed.title = "Serversplash geändert"
        embed.description = f"Der Serversplash wurde von {before.splash} zu {after.splash} geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.discovery_splash != after.discovery_splash:
        embed = default_event_embed
        embed.title = "Serverdiscovery Splash geändert"
        embed.description = f"Der Serverdiscovery Splash wurde von {before.discovery_splash} zu {after.discovery_splash} geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.system_channel != after.system_channel:
        embed = default_event_embed
        embed.title = "Serversystem Channel geändert"
        embed.description = f"Der Serversystem Channel wurde von <#{before.system_channel}> zu <#{after.system_channel}> geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.rules_channel != after.rules_channel:
        embed = default_event_embed
        embed.title = "Serverrules Channel geändert"
        embed.description = f"Der Serverrules Channel wurde von <#{before.rules_channel}> zu <#{after.rules_channel}> geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.public_updates_channel != after.public_updates_channel:
        embed = default_event_embed
        embed.title = "Serverpublic_updates_channel geändert"
        embed.description = f"Der Serverpublic_updates_channel wurde von <#{before.public_updates_channel}> zu <#{after.public_updates_channel}> geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.preferred_locale != after.preferred_locale:
        embed = default_event_embed
        embed.title = "Serverpreferred_locale geändert"
        embed.description = f"Der Serverpreferred_locale wurde von **{before.preferred_locale}** zu **{after.preferred_locale}** geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.afk_channel != after.afk_channel:
        embed = default_event_embed
        embed.title = "Serverafk Channel geändert"
        embed.description = f"Der Serverafk Channel wurde von <#{before.afk_channel}> zu <#{after.afk_channel}> geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.afk_timeout != after.afk_timeout:
        x = before.afk_timeout
        x1 = x/60
        y = after.afk_timeout
        y1 = y/60
        embed = default_event_embed
        embed.title = "Serverafk Timeout geändert"
        embed.description = f"Der Serverafk Timeout wurde von **{x1} Minuten** zu **{y1} Minuten** geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.default_notifications != after.default_notifications:
        embed = default_event_embed
        embed.title = "Serverdefault notifications geändert"
        embed.description = f"Die Serverdefault Benachrichtigungen wurde von **{before.default_notifications}** zu **{after.default_notifications}** geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.explicit_content_filter != after.explicit_content_filter:
        embed = default_event_embed
        embed.title = "Serverexplicit_content_filter geändert"
        embed.description = f"Der Serverexplicit content filter wurde von **{before.explicit_content_filter}** zu **{after.explicit_content_filter}** geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)

    if before.mfa_level != after.mfa_level:
        embed = default_event_embed
        embed.title = "Servermfa level geändert"
        embed.description = f"Der Servermfa level wurde von **{before.mfa_level}** zu **{after.mfa_level}** geändert"
        await bot.get_channel(guild_tracker_channel).send(embed=embed)


#channel tracker
@bot.event
async def on_guild_channel_create(channel):
    embed = default_event_embed
    embed.title = "Channel erstellt"
    embed.description = f"Der Channel **{channel.name}** wurde erstellt"
    await bot.get_channel(channel_tracker_channel).send(embed=embed)

@bot.event
async def on_guild_channel_delete(channel):
    embed = default_event_embed
    embed.title = "Channel gelöscht"
    embed.description = f"Der Channel **{channel.name}** wurde gelöscht"
    await bot.get_channel(channel_tracker_channel).send(embed=embed)

@bot.event
async def on_guild_channel_update(before, after):
    if before.name != after.name:
        embed = default_event_embed
        embed.title = "Channelname geändert"
        embed.description = f"Der Channelname wurde von **{before.name}** zu **{after.name}** geändert"
        await bot.get_channel(channel_tracker_channell).send(embed=embed)

    if before.topic != after.topic:
        embed = default_event_embed
        embed.title = "Channeltopic geändert"
        embed.description = f"Der Channel **{before.name}** hat ein neues Topic: {after.topic}"
        await bot.get_channel(channel_tracker_channel).send(embed=embed)

    if before.position != after.position:
        embed = default_event_embed
        embed.title = "Channelposition geändert"
        embed.description = f"Der Channelposition wurde von **{before.position}** zu **{after.position}** geändert"
        await bot.get_channel(channel_tracker_channel).send(embed=embed)


    if before.slowmode_delay != after.slowmode_delay:
        embed = default_event_embed
        embed.title = "Channelslowmode delay geändert"
        embed.description = f"Der Channelslowmode delay von {before.name} wurde von **{before.slowmode_delay}** zu **{after.slowmode_delay}** geändert"
        await bot.get_channel(channel_tracker_channel).send(embed=embed)

    if before.nsfw != after.nsfw:
        embed = default_event_embed
        embed.title = "Channelnsfw geändert"
        embed.description = f"Der Channelnsfw von {before.name} wurde von **{before.nsfw}** zu **{after.nsfw}** geändert"
        await bot.get_channel(channel_tracker_channel).send(embed=embed)

    if before.category != after.category:
        embed = default_event_embed
        embed.title = "Channelcategory geändert"
        embed.description = f"Der Channelcategory wurde von **{before.category}** zu **{after.category}** geändert"
        await bot.get_channel(channel_tracker_channel).send(embed=embed)


#invite tracker
@bot.event
async def on_invite_create(invite):
    embed = default_event_embed
    embed.title = "Invite erstellt"
    embed.description = f"Der Invite **{invite.code}** wurde erstellt"
    await bot.get_channel(invite_tracker_channel).send(embed=embed)

@bot.event
async def on_invite_delete(invite):
    embed = default_event_embed
    embed.title = "Invite gelöscht"
    embed.description = f"Der Invite **{invite.code}** wurde gelöscht"
    await bot.get_channel(invite_tracker_channel).send(embed=embed)

#role tracker
@bot.event
async def on_guild_role_create(role):
    perms = role.permissions
    embed = default_event_embed
    embed.title = "Role erstellt"
    embed.description = f"Die Role **{role.name}** wurde erstellt"
    embed.add_field(name="Permissions", value=f"{perms}")
    await bot.get_channel(role_tracker_channel).send(embed=embed)

@bot.event
async def on_guild_role_delete(role):
    embed = default_event_embed
    embed.title = "Role gelöscht"
    embed.description = f"Die Role **{role.name}** wurde gelöscht"
    await bot.get_channel(role_tracker_channel).send(embed=embed)

@bot.event
async def on_guild_role_update(before, after):
    if before.name != after.name:
        embed = default_event_embed
        embed.title = "Rolename geändert"
        embed.description = f"Der Rolename wurde von **{before.name}** zu **{after.name}** geändert"
        await bot.get_channel(role_tracker_channel).send(embed=embed)

    if before.color != after.color:
        embed = default_event_embed
        embed.title = "Rolecolor geändert"
        embed.description = f"Die Rolecolor von {before.name} wurde von **{before.color}** zu **{after.color}** geändert"
        await bot.get_channel(role_tracker_channel).send(embed=embed)

    if before.permissions != after.permissions:
        embed = default_event_embed
        embed.title = "Rolepermissions geändert"
        embed.description = f"Die Rolepermissions von {before.name} wurden von **{before.permissions}** zu **{after.permissions}** geändert"
        await bot.get_channel(role_tracker_channel).send(embed=embed)

#member tracker
@bot.event
async def on_member_join(member):
    x = datetime.datetime.now()
    discriminator = member.discriminator
    id = member.id
    embed = default_event_embed
    embed.title = "Member joined"
    embed.description = f"Der Member **{member}** ist dem Server beigetreten"
    embed.add_field(name="Discriminator", value=f"{discriminator}")
    embed.add_field(name="ID", value=f"{id}")
    embed.set_footer(text=f"{x}")
    await bot.get_channel(member_tracker_channel).send(embed=embed)

@bot.event
async def on_member_remove(member):
    x = datetime.datetime.now()
    discriminator = member.discriminator
    id = member.id
    embed = default_event_embed
    embed.title = "Member left"
    embed.description = f"Der Member **{member}** hat den Server verlassen"
    embed.add_field(name="Discriminator", value=f"{discriminator}")
    embed.add_field(name="ID", value=f"{id}")
    embed.set_footer(text=f"{x}")
    await bot.get_channel(member_tracker_channel).send(embed=embed)

@bot.event
async def on_member_update(before: disnake.member, after: disnake.member):
    user: disnake.user
    member: disnake.member
    if before.name != after.name:
        embed = default_event_embed
        embed.title = "Membername geändert"
        embed.description = f"Der Membername wurde von **{before.name}** zu **{after.name}** geändert"
        await bot.get_channel(member_tracker_channel).send(embed=embed)

    if before.nick != after.nick:
        user: disnake.user
        member: disnake.member
        discriminator = user.discriminator
        id = member.id
        embed = default_event_embed
        embed.title = "Membernick geändert"
        embed.description = f"Der Membernick von {before.name} + {discriminator} + '('{id}')' wurde von **{before.nick}** zu **{after.nick}** geändert"
        await bot.get_channel(member_tracker_channel).send(embed=embed)

    if before.roles != after.roles:
        user: disnake.user = after
        member: disnake.member = after
        discriminator = user.discriminator
        id = member.id
        embed = default_event_embed
        embed.title = "Memberroles geändert"
        embed.description = f"Die Memberroles von {before.name} + {discriminator} + '('{id}')' wurden von **{before.roles}** zu **{after.roles}** geändert"
        await bot.get_channel(member_tracker_channel).send(embed=embed)

#Status Task erstellen
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

    else:
        print('Bot ist offline.')
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
    await ctx.send(" Bot ist offline.")
    await bot.close()
    sys.exit(0)

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print(f'{filename} wurde geladen!')
            bot.reload_extension(f'cogs.{filename[:-3]}')
    await ctx.send("Cogs wurden neu geladen.")

@bot.command()
@commands.is_owner()
async def cogslist(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await ctx.send(f'{filename} ')

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} wurde geladen.')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} wurde entladen.')

#Error Handling

@bot.slash_command(description="Antwortet mit Welt!")
async def hello(inter):
    await inter.response.send_message("Welt")



@bot.slash_command(description="Sendet ein Küsschen an den User")
async def kuss(inter, person: disnake.Member):
    await inter.response.send_message('Hey ' + person.mention + ' Hier ist ein Küsschen von ' + inter.author.mention + ' :kissing_heart:')
started = False


#bot ausführen
import ItsAlex
ItsAlexKey = ItsAlex.TOKEN
bot.run(ItsAlexKey)
