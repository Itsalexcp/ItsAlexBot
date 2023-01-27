import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands
from defaults.style import role_embed


class RoleUpdateEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_update(self, before: disnake.Role, after: disnake.Role):
        """This will be for the guildUpdate event."""
        bot = self.bot
        if before.name != after.name:
            embed = role_embed(title="Rolle verändert",
                               name=after.name,
                               id=before.id, )
            embed.add_field(name="Art der Änderung", value=f"Name von {before.name} zu {after.name} verändert ")
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

        if before.color != after.color:
            embed = role_embed(title="Rolle verändert",
                               name=after.name,
                               id=before.id, )
            embed.add_field(name="Art der Änderung", value=f"Name von {before.color} zu {after.color} verändert ")
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

        if before.hoist != after.hoist:
            embed = role_embed(title="Rolle verändert",
                               name=after.name,
                               id=before.id, )
            if after.hoist is True:
                embed.add_field(name="Art der Änderung", value=f"Rolle wird rechts angezeigt")
            else:
                embed.add_field(name="Art der Änderung", value=f"Rolle wird nicht angezeigt")
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

        if before.mentionable != after.mentionable:
            embed = role_embed(title="Rolle verändert",
                               name=after.name,
                               id=before.id, )
            if after.mentionable is True:
                embed.add_field(name="Art der Änderung", value=f"Rolle kann erwähnt werden")
            else:
                embed.add_field(name="Art der Änderung", value=f"Rolle kann nicht mehr erwähnt werden")
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

        if before.permissions != after.permissions:
            embed = role_embed(title="Rolle verändert",
                               name=after.name,
                               id=before.id, )
            embed.add_field(name="Art der Änderung", value=f"Perms {before.permissions} zu {after.permissions} verändert ")
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(RoleUpdateEvent(bot))
