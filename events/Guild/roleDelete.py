import disnake
import defaults
from defaults import style
from defaults.style import role_embed
from defaults import emojis
from defaults import channels
from disnake.ext import commands


class RoleDeleteEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role: disnake.Role):
        bot = self.bot
        embed = role_embed(name=role.name,
                           title="Rolle gelöscht",
                           id=role.id, )
        await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(RoleDeleteEvent(bot))
