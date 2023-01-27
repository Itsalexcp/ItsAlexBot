import disnake
from disnake.ext import commands
import datetime
import os
import asyncio
import defaults
from defaults import emojis
from defaults import style


class CopyCategory(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def copycat(self, inter: disnake.ApplicationCommandInteraction, category: disnake.CategoryChannel):
        """Kopiert eine Kategorie samt Berechtigungen"""
        await inter.response.defer()
        guild = inter.guild
        category = disnake.utils.get(guild.categories, name=category.name)
        if category is None:
            return await inter.followup.send("Kategorie nicht gefunden.")

        # Create new category
        new_category = await guild.create_category(name=category.name + " - Kopie")
        await new_category.edit(position=category.position)
        await new_category.edit(reason=f"Kategorie kopiert von {inter.author}")
        perms = category.overwrites
        for perm in perms:
            await new_category.set_permissions(perm, overwrite=perms[perm])

            await inter.followup.send(f"Kopiere Kategorie {category.name} nach {new_category.name}.")


def setup(bot):
    bot.add_cog(CopyCategory(bot))
