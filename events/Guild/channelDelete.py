import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands
from defaults.style import channel_embed


class ChannelDeleteEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: disnake.abc.GuildChannel):
        bot = self.bot
        embed = channel_embed(title="Channel gelöscht",
                              id=channel.id,
                              created_at=channel.created_at,
                              category=channel.category, )
        await bot.get_channel(defaults.channels.channel_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(ChannelDeleteEvent(bot))
