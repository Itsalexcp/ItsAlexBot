import disnake
from datetime import datetime
import pytz

tz = pytz.timezone('Europe/Berlin')

datetime.now(tz).strftime("%d.%m.%Y um %H:%M:%S")
created_ats = datetime.now(tz).strftime("%d.%m.%Y um %H:%M:%S")


# event embed
def channel_embed(title=None,
                  name=None,
                  id=None,
                  created_at=None,
                  category=None,
                  jump_url=None,
                  position=None):
    embed = disnake.Embed(
        color=primaryColor,
        timestamp=datetime.now(tz)
    )
    if title is not None:
        embed.title = title
    if name is not None:
        embed.add_field(name='Name:', value=name, inline=False)
    if id is not None:
        embed.add_field(name='ID:', value=id, inline=False)
    if created_at is not None:
        embed.add_field(name='Erstellt am:', value=created_ats, inline=False)
    if category is not None:
        embed.add_field(name='Kategorie:', value=category, inline=False)
    if jump_url is not None:
        embed.add_field(name='Channel Link:', value=f'[Zum Channel]({jump_url})', inline=False)
    if position is not None:
        embed.add_field(name='Position:', value=position, inline=False)
    embed.set_author(name="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    embed.set_footer(text="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    return embed


def role_embed(title=None,
               name=None,
               id=None,
               hoist=None,
               mentionable=None,
               role_color=None,
               created_at=None,
               position=None):
    embed = disnake.Embed(
        color=primaryColor,
        timestamp=datetime.now(tz)
    )
    if title is not None:
        embed.title = title
    if name is not None:
        embed.add_field(name='Name:', value=name, inline=False)
    if hoist is not None:
        embed.add_field(name='Gelistet:', value=hoist, inline=False)
    if mentionable is not None:
        embed.add_field(name='Erwähnbar', value=mentionable, inline=False)
    if role_color is not None:
        embed.add_field(name='Farbe', value=role_color, inline=False)
    if id is not None:
        embed.add_field(name='ID:', value=id, inline=False)
    if created_at is not None:
        embed.add_field(name='Erstellt am:', value=created_ats, inline=False)
    if position is not None:
        embed.add_field(name='Position:', value=position, inline=False)
    embed.set_author(name="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    embed.set_footer(text="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    return embed


def guild_embed(title=None,
                name=None,
                id=None,
                afk_channel=None,
                afk_timeout=None,
                created_at=None,
                default_message_notifications=None,
                description=None,
                explicit_content_filter=None,
                icon=None,
                mfa_level=None,
                owner=None,
                verification_level=None,
                vanity_url_code=None,
                ):
    embed = disnake.Embed(
        color=primaryColor,
        timestamp=datetime.now(tz)
    )
    if title is not None:
        embed.title = title
    if name is not None:
        embed.add_field(name='Servername:', value=name, inline=False)
    if id is not None:
        embed.add_field(name='ServerID:', value=id, inline=False)
    if afk_channel is not None:
        embed.add_field(name='AFK Kanal:', value=afk_channel, inline=False)
    if afk_timeout is not None:
        embed.add_field(name='AFK Timeout:', value=afk_timeout, inline=False)
    if created_at is not None:
        embed.add_field(name='Erstellt am:', value=created_ats, inline=False)
    if default_message_notifications is not None:
        embed.add_field(name='Systembenachrichtigungen:', value=default_message_notifications, inline=False)
    if description is not None:
        embed.add_field(name='Beschreibung:', value=description, inline=False)
    if explicit_content_filter is not None:
        embed.add_field(name='Nachrichten durchsuchen', value=explicit_content_filter, inline=False)
    if mfa_level is not None:
        embed.add_field(name='MFA Level:', value=mfa_level, inline=False)
    if owner is not None:
        embed.add_field(name='Owner:', value=owner, inline=False)
    if verification_level is not None:
        embed.add_field(name='Verifizierungs Level', value=verification_level, inline=False)
    if vanity_url_code is not None:
        embed.add_field(name='Vanity URL Code:', value=vanity_url_code, inline=False)
    if icon is not None:
        embed.set_thumbnail(url=icon)

    embed.set_author(name="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    embed.set_footer(text="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    return embed


def message_embed(title=None,
                  author=None,
                  content=None,
                  channel=None,
                  attachments=None,
                  id=None,
                  created_at=None,):
    embed = disnake.Embed(
        color=primaryColor,
        timestamp=datetime.now(tz)
    )
    if title is not None:
        embed.title = title
    if author is not None:
        embed.add_field(name='Autor:', value=author, inline=False)
    if content is not None:
        embed.add_field(name='Nachricht:', value=content, inline=False)
    if channel is not None:
        embed.add_field(name='Channel:', value=channel, inline=False)
    if attachments is not None:
        embed.add_field(name='Attachments:', value=attachments, inline=False)
    if id is not None:
        embed.add_field(name='NachrichtenID:', value=id, inline=False)
    if created_at is not None:
        embed.add_field(name='Erstellt am:', value=created_ats, inline=False)
    embed.set_author(name="Message", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    embed.set_footer(text="Message", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    return embed


# colors
primaryColor = 0xe6e600
secondaryColor = 0x33ccff
accentColor = 0x6a329f
trueColor = 0xa0db8e
falseColor = 0xe60000

# stats embed
status_on_embed = disnake.Embed(
    color=disnake.Colour.green(),
    timestamp=datetime.now(tz)
)
status_on_embed.set_author(
    name="Ich bin online",
    icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
             "/AppIconGhostStation.png")
status_on_embed.set_footer(
    text="Dies ist ein Service von ItsAlex Enterprise",
)

status_off_embed = disnake.Embed(
    color=disnake.Colour.red(),
    timestamp=datetime.now(tz)
)
status_off_embed.set_author(
    name="Ich bin offline",
    icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
             "/AppIconGhostStation.png")
status_off_embed.set_footer(
    text="Dies ist ein Service von ItsAlex Enterprise",
)
