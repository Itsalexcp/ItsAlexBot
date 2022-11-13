import disnake

# event embed
event_embed = disnake.Embed(
    color=disnake.Colour.yellow(),
    timestamp=disnake.utils.utcnow()
)
event_embed.set_author(
    name="Ich habe etwas aufgezeichnet",
    icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1039309745128996864"
             "/AppIconGhostStation.png")
event_embed.set_footer(
    text="Dies ist ein Service von ItsAlex Enterprise",
)
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
