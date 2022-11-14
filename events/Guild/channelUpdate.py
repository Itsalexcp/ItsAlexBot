import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands
from defaults.style import event_embed


class ChannelUpdateEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before: disnake.abc.GuildChannel, after: disnake.abc.GuildChannel):
        bot = self.bot
        if before.name != after.name:
            embed = event_embed(title="Channel verändert",
                                name=before.name,
                                id=before.id,
                                created_at=before.created_at,
                                category=before.category,
                                jump_url=before.jump_url,
                                position=before.position)
            embed.add_field(name="Art der Änderung", value=f"Name von {before.name} zu {after.name} verändert ")
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

        if before.topic != after.topic:
            embed = event_embed(title="Channel verändert",
                                name=after.name if before.name != after.name else before.name,
                                id=before.id,
                                created_at=before.created_at,
                                category=before.category,
                                jump_url=before.jump_url,
                                position=before.position)
            embed.add_field(name="Art der Änderung", value=f"Thema von {before.topic} zu {after.topic} verändert ")
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

        if before.position != after.position:
            embed = event_embed(title="Channel verändert",
                                name=after.name if before.name != after.name else before.name,
                                id=before.id,
                                created_at=before.created_at,
                                category=before.category,
                                jump_url=before.jump_url,
                                position=before.position)
            embed.add_field(name="Art der Änderung", value=f"Position des Kanals von {before.position} zu {after.position} verändert ")
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

        if before.category != after.category:
            embed = event_embed(title="Channel verändert",
                                name=after.name if before.name != after.name else before.name,
                                id=before.id,
                                created_at=before.created_at,
                                category=before.category,
                                jump_url=before.jump_url,
                                position=before.position)
            embed.add_field(name="Art der Änderung", value=f"Kategorie von {before.category} zu {after.category} verändert ")
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

        if before.slowmode_delay != after.slowmode_delay:
            embed = event_embed(title="Channel verändert",
                                name=after.name if before.name != after.name else before.name,
                                id=before.id,
                                created_at=before.created_at,
                                category=before.category,
                                jump_url=before.jump_url,
                                position=before.position)
            if after.slowmode_delay == 0:
                embed.add_field(name="Art der Änderung", value=f"Slowmode deaktiviert")
            if after.slowmode_delay > 0:
                embed.add_field(name="Art der Änderung", value=f"Slowmode aktiviert mit einer Dauer von {after.slowmode_delay} Sekunden")
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)

        if before.nsfw != after.nsfw:
            embed = event_embed(title="Channel verändert",
                                name=after.name if before.name != after.name else before.name,
                                id=before.id,
                                created_at=before.created_at,
                                category=before.category,
                                jump_url=before.jump_url,
                                position=before.position)
            if not before.nsfw:
                embed.add_field(name="Art der Änderung", value=f"NSFW wurde aktiviert")
            else:
                embed.add_field(name="Art der Änderung", value=f"NSFW wurde deaktiviert")
            await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(ChannelUpdateEvent(bot))
