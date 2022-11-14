import disnake


# event embed
def event_embed(title=None,
                name=None,
                id=None,
                created_at=None,
                category=None,
                jump_url=None,
                position=None):
    embed = disnake.Embed(
        color=primaryColor,
        timestamp=disnake.utils.utcnow()
    )
    if title is not None:
        embed.title = title
    if name is not None:
        embed.add_field(name='Name:', value=name, inline=False)
    if id is not None:
        embed.add_field(name='ID:', value=id, inline=False)
    if created_at is not None:
        embed.add_field(name='Erstellt am:', value=created_at, inline=False)
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
        timestamp=disnake.utils.utcnow()
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
        embed.add_field(name='Erstellt am:', value=created_at, inline=False)
    if position is not None:
        embed.add_field(name='Position:', value=position, inline=False)
    embed.set_author(name="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
    embed.set_footer(text="Event Tracker", icon_url="https://cdn.discordapp.com/attachments/1041138068901601400/1041423420845473792/DE_ServerVerifiedBlue.png")
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
    timestamp=disnake.utils.utcnow()
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
    timestamp=disnake.utils.utcnow()
)
status_off_embed.set_author(
    name="Ich bin offline",
    icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
             "/AppIconGhostStation.png")
status_off_embed.set_footer(
    text="Dies ist ein Service von ItsAlex Enterprise",
)
