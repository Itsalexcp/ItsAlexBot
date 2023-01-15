import disnake
from datetime import datetime
import pytz
from defaults import emojis

# timeformat
tz = pytz.timezone('Europe/Berlin')
datetime.now(tz).strftime("%d.%m.%Y um %H:%M:%S")
created_ats = datetime.now(tz).strftime("%d.%m.%Y um %H:%M:%S")
joined_ats = datetime.now(tz).strftime("%d.%m.%Y um %H:%M:%S")
left_ats = datetime.now(tz).strftime("%d.%m.%Y um %H:%M:%S")

# colors
primaryColor = 0xe6e600
secondaryColor = 0x33ccff
accentColor = 0x6a329f
trueColor = 0xa0db8e
falseColor = 0xe60000


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
        embed.add_field(name=f'{emojis.IconChannelText} Name:', value=name, inline=False)
    if id is not None:
        embed.add_field(name=f'{emojis.IconId} ID:', value=id, inline=False)
    if created_at is not None:
        embed.add_field(name=f'{emojis.IconClock} Erstellt am:', value=created_ats, inline=False)
    if category is not None:
        embed.add_field(name=f'{emojis.IconUnread} Kategorie:', value=category, inline=False)
    if jump_url is not None:
        embed.add_field(name=f'{emojis.IconLink} Channel Link:', value=f'[Zum Channel]({jump_url})', inline=False)
    if position is not None:
        embed.add_field(name=f'{emojis.CThreads}Position:', value=position, inline=False)
    embed.set_author(name="Kanal event", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
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
        embed.add_field(name=f'Name:', value=name, inline=False)
    if hoist is not None:
        embed.add_field(name=f'Gelistet:', value=hoist, inline=False)
    if mentionable is not None:
        embed.add_field(name=f'Erwähnbar', value=mentionable, inline=False)
    if role_color is not None:
        embed.add_field(name=f'Farbe', value=role_color, inline=False)
    if id is not None:
        embed.add_field(name=f'{emojis.IconId} ID:', value=id, inline=False)
    if created_at is not None:
        embed.add_field(name=f'{emojis.IconClock} Erstellt am:', value=created_ats, inline=False)
    if position is not None:
        embed.add_field(name=f'{emojis.CThreads} Position:', value=position, inline=False)
    embed.set_author(name="Rollen Event", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
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
        embed.add_field(name=f'{emojis.IconServerInsights} Servername:', value=name, inline=False)
    if id is not None:
        embed.add_field(name=f'{emojis.IconId} ServerID:', value=id, inline=False)
    if afk_channel is not None:
        embed.add_field(name=f'{emojis.IconChannelText} AFK Kanal:', value=afk_channel, inline=False)
    if afk_timeout is not None:
        embed.add_field(name=f'{emojis.IconSlowMode} AFK Timeout:', value=afk_timeout, inline=False)
    if created_at is not None:
        embed.add_field(name=f'{emojis.IconClock}Erstellt am:', value=created_ats, inline=False)
    if default_message_notifications is not None:
        embed.add_field(name=f'{emojis.IconNotification} Systembenachrichtigungen:', value=default_message_notifications, inline=False)
    if description is not None:
        embed.add_field(name=f'{emojis.ServerDiscovery} Beschreibung:', value=description, inline=False)
    if explicit_content_filter is not None:
        embed.add_field(name=f'{emojis.IconSearch} Nachrichten durchsuchen', value=explicit_content_filter, inline=False)
    if mfa_level is not None:
        embed.add_field(name=f'{emojis.BanHammer} MFA Level:', value=mfa_level, inline=False)
    if owner is not None:
        embed.add_field(name=f'{emojis.ServerOwner} Owner:', value=owner, inline=False)
    if verification_level is not None:
        embed.add_field(name=f'{emojis.Verified} Verifizierungs Level', value=verification_level, inline=False)
    if vanity_url_code is not None:
        embed.add_field(name=f'{emojis.ServerLevel3} Vanity URL Code:', value=vanity_url_code, inline=False)
    if icon is not None:
        embed.set_thumbnail(url=icon)

    embed.set_author(name="Server Event", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    embed.set_footer(text="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    return embed


def message_embed(title=None,
                  author=None,
                  content=None,
                  channel=None,
                  attachments=None,
                  id=None,
                  created_at=None, ):
    embed = disnake.Embed(
        color=primaryColor,
        timestamp=datetime.now(tz)
    )
    if title is not None:
        embed.title = title
    if author is not None:
        embed.add_field(name=f'{emojis.IconMembers} Autor:', value=author, inline=False)
    if content is not None:
        embed.add_field(name=f'{emojis.IconThread} Nachricht:', value=content, inline=False)
    if channel is not None:
        embed.add_field(name=f'{emojis.IconChannelText} Channel:', value=channel, inline=False)
    if attachments is not None:
        embed.add_field(name=f'{emojis.IconAttachment} Attachments:', value=attachments, inline=False)
    if id is not None:
        embed.add_field(name=f'{emojis.IconId} NachrichtenID:', value=id, inline=False)
    if created_at is not None:
        embed.add_field(name=f'{emojis.IconClock} Erstellt am:', value=created_ats, inline=False)
    embed.set_author(name="Message Event", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    embed.set_footer(text="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    return embed


def voicestate_embed(title=None,
                     member=None,
                     channel=None,
                     id=None,
                     joined_at=None,
                     left_at=None,
                     ):
    embed = disnake.Embed(
        color=primaryColor,
        timestamp=datetime.now(tz)
    )
    if title is not None:
        embed.title = title
    if member is not None:
        embed.add_field(name=f'{emojis.IconMembers} Member:', value=member, inline=False)
    if channel is not None:
        embed.add_field(name=f'{emojis.IconChannelText} Channel:', value=channel, inline=False)
    if id is not None:
        embed.add_field(name=f'{emojis.IconId} ID:', value=id, inline=False)
    if joined_at is not None:
        embed.add_field(name=f'{emojis.ArrowJoin} Beigetreten am:', value=joined_ats, inline=False)
    if left_at is not None:
        embed.add_field(name=f'{emojis.ArrowLeave} Verlassen am:', value=left_ats, inline=False)
    embed.set_author(name="VoiceLog", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    embed.set_footer(text="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    return embed


def member_embed(title=None,
                 name=None,
                 discriminator=None,
                 id=None,
                 created_at=None,
                 joined_at=None,
                 left_at=None,
                 roles=None,
                 nick=None,
                 premium_since=None,
                 is_on_mobile=None,
                 ):
    embed = disnake.Embed(
        color=primaryColor,
        timestamp=datetime.now(tz)
    )
    if title is not None:
        embed.title = title
    if name is not None:
        embed.add_field(name=f'{emojis.IconMembers} Name:', value=name, inline=False)
    if discriminator is not None:
        embed.add_field(name=f'{emojis.IconChannelText} Discriminator:', value=f"#{discriminator}", inline=False)
    if id is not None:
        embed.add_field(name=f'{emojis.IconId} ID:', value=id, inline=False)
    if created_at is not None:
        embed.add_field(name=f'{emojis.IconClock} Erstellt am:', value=created_at, inline=False)
    if left_at is not None:
        embed.add_field(name=f'{emojis.ArrowLeave} Verlassen am:', value=left_at, inline=False)
    if joined_at is not None:
        embed.add_field(name=f'{emojis.ArrowJoin} Beigetreten am:', value=joined_at, inline=False)
    if roles is not None:
        embed.add_field(name=f'{emojis.RichPresence} Rollen:', value=roles, inline=False)
    if nick is not None:
        embed.add_field(name=f'{emojis.IconQuote} Nickname:', value=nick, inline=False)
    if premium_since is not None:
        embed.add_field(name=f'{emojis.NitroEmoji} Nitro seit:', value=premium_since, inline=False)
    if is_on_mobile is not None:
        if is_on_mobile is True:
            embed.add_field(name='Gerät:', value=f"{emojis.StatusPhoneOnline} Handy", inline=False)
        if is_on_mobile is False:
            embed.add_field(name='Gerät:', value=f"{emojis.IconScreenshare} PC", inline=False)

    embed.set_author(name="Mitglied Event", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    embed.set_footer(text="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    return embed


def invite_embed(title=None,
                 inviter=None,
                 guild=None,
                 code=None,
                 uses=None,
                 max_uses=None,
                 max_age=None,
                 temporary=None,
                 created_at=None,
                 ):
    embed = disnake.Embed(
        color=primaryColor,
        timestamp=datetime.now(tz)
    )
    if title is not None:
        embed.title = title
    if inviter is not None:
        embed.add_field(name=f'{emojis.IconMembers} Ersteller', value=inviter, inline=False)
    if guild is not None:
        embed.add_field(name=f'{emojis.ServerDiscovery} Server', value=guild, inline=False)
    if code is not None:
        embed.add_field(name=f'{emojis.IconInvite} Code:', value=code, inline=False)
    if uses is not None:
        embed.add_field(name=f'{emojis.IconInvite} Verwendungen:', value=uses, inline=False)
    if max_uses is not None:
        embed.add_field(name=f'{emojis.IconInvite} Maximale Verwendungen:', value=max_uses, inline=False)
    if max_age is not None:
        embed.add_field(name=f'{emojis.IconClock} Gültigkeit:', value=max_age, inline=False)
    if temporary is not None:
        if temporary is True:
            embed.add_field(name='Temporär:', value="Ja", inline=False)
        if temporary is False:
            embed.add_field(name='Temporär:', value="Nein", inline=False)
    if created_at is not None:
        embed.add_field(name=f'{emojis.AuditLinkAdd} Erstellt am:', value=created_at, inline=False)
    embed.set_author(name="Invite Event", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    embed.set_footer(text="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    return embed


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
