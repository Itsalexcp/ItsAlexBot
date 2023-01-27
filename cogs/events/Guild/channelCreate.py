import disnake
import defaults
from defaults import style
from defaults.style import channel_embed
from defaults import emojis
from defaults import channels
from disnake.ext import commands


class ChannelCreateEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: disnake.abc.GuildChannel):
        bot = self.bot
        embed = channel_embed(name=channel.name,
                              title=f"{emojis.AuditChannelAdd}Channel erstellt",
                              id=channel.id,
                              created_at=channel.created_at,
                              category=channel.category,
                              jump_url=channel.jump_url,
                              position=channel.position)
        await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(ChannelCreateEvent(bot))
