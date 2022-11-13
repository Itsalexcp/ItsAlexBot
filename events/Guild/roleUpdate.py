import disnake
import defaults
from defaults import style
from defaults import emojis
from defaults import channels
from disnake.ext import commands


class RoleUpdateEvent(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_role_update(self, role: disnake.Role, before: disnake.Role, after: disnake.Role):
        """This will be for the guildUpdate event."""
        bot = self.bot
        if before.name != after.name:
            embed = defaults.style.event_embed
            embed.title = "Rollenname geändert"
            embed.description = f"Der Rollenname wurde von **{before.name}** zu **{after.name}** geändert"
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

        if before.color != after.color:
            embed = defaults.style.event_embed
            embed.title = "Rollenfarbe geändert"
            embed.description = f"Die Rollenfarbe von {role.name} wurde von **{before.color}** zu **{after.color}** geändert"
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

        if before.hoist != after.hoist:
            embed = defaults.style.event_embed
            embed.title = "Rollenposition geändert"
            embed.description = f"Die Rollenposition von {role.name} wurde von **{before.hoist}** zu **{after.hoist}** geändert"
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

        if before.mentionable != after.mentionable:
            embed = defaults.style.event_embed
            embed.title = "Mentionable geändert"
            embed.description = f"Erwähnbarkeit von {role.name} wurde von **{before.mentionable}** zu **{after.mentionable}** geändert"
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

        if before.permissions != after.permissions:
            embed = defaults.style.event_embed
            embed.title = "Rollenrechte geändert"
            embed.description = f"Die Rollenrechte von {role.name} wurden von **{before.permissions}** zu **{after.permissions}** geändert"
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

        if before.position != after.position:
            embed = defaults.style.event_embed
            embed.title = "Rollenposition geändert"
            embed.description = f"Die Rollenposition von {role.name} wurde von **{before.position}** zu **{after.position}** geändert"
            await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role: disnake.Role):
        bot = self.bot
        embed = defaults.style.event_embed
        embed.title = "Rolle erstellt"
        embed.description = f"Die Rolle {role.name} wurde erstellt"
        embed.add_field(name="Farbe", value=role.color)
        embed.add_field(name="Erwähnbar", value=role.mentionable)
        embed.add_field(name="Position", value=role.position)
        embed.add_field(name="Rechte", value=role.permissions)
        await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role: disnake.Role):
        bot = self.bot
        embed = defaults.style.event_embed
        embed.title = "Rolle gelöscht"
        embed.description = f"Die Rolle {role.name} wurde gelöscht"
        await bot.get_channel(defaults.channels.role_tracker).send(embed=embed)


def setup(bot):
    bot.add_cog(RoleUpdateEvent(bot))
