import disnake
import defaults
from defaults import style
from defaults.style import role_embed
from defaults import emojis
from defaults import channels
from disnake.ext import commands


class RoleCreateEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_create(self, role: disnake.Role):
        bot = self.bot
        embed = role_embed(name=role.name,
                           title=f"Rolle erstellt {role.mention}",
                           id=role.id,
                           role_color=role.color,
                           created_at=role.created_at,
                           position=role.position, )
        if role.mentionable is True:
            embed.add_field(name="Erwähnbar", value=f"Rolle kann erwähnt werden")
        else:
            embed.add_field(name="Erwähnbar", value=f"Rolle kann nicht erwähnt werden")
        if role.hoist is True:
            embed.add_field(name="Anzeige", value=f"Rolle wird rechts angezeigt")
        else:
            embed.add_field(name="Anzeige", value=f"Rolle wird nicht angezeigt")
        await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(RoleCreateEvent(bot))
