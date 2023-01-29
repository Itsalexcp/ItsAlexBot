import disnake
from disnake.ext import commands
import datetime
import os
import asyncio
import random
import string

from disnake.utils import search_directory

import defaults
from defaults import emojis
from defaults import style


async def generate_password(length=16):
    """Generate a strong, secure and unique password of the specified length.
    Default length is 16 characters.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


class PasswordGenerator(commands.Cog):
    """Passwort Generator"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="password", description="Generiert ein zufälliges Passwort.")
    async def password(self, inter: disnake.ApplicationCommandInteraction, length: int):
        """Generiert ein zufälliges Passwort."""
        passwordembed = disnake.Embed(
            title="Passwort Generator",
            description="Dein Passwort wurde generiert.",
            color=disnake.Colour.green(),
            timestamp=datetime.datetime.now(),
        )
        passwordembed.set_author(
            name=inter.author.name + "#" + inter.author.discriminator,
            icon_url=inter.author.avatar
        )
        passwordembed.set_footer(text="Powered by itsalex.cp#0001", icon_url="https://cdn.discordapp.com/attachments/1038885667360493568/1043262304726286376/DE_SnowsgivingClydeLight.png")
        passwordembed.add_field(name=f"{emojis.IconQuote} Länge", value=length, inline=False)
        passwordembed.add_field(name=f"{emojis.IconLock} Passwort", value=await generate_password(length), inline=False)
        await inter.response.send_message(embed=passwordembed)


def setup(bot: commands.Bot):
    bot.add_cog(PasswordGenerator(bot))
