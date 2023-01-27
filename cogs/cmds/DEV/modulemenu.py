import disnake
from disnake.ext import commands
import datetime
import os
import asyncio
from disnake.utils import search_directory

import defaults
from defaults import emojis
from defaults import style


def search_cogs():
    for folder, subfolder, file in os.walk("cogs/"):
        for filename in file:
            if filename.endswith(".py"):
                filenamepath = os.path.join(folder, filename)
                filenamepath = filenamepath.replace("\\", ".")
                filenamepath = filenamepath.replace("/", ".")
                filenamepath = filenamepath.replace(".py", "")
                yield filenamepath


class MenuButtons(disnake.ui.View):
    def __init__(self, bot: commands.Bot):
        super().__init__(timeout=360.0)
        self.bot = bot

    @disnake.ui.button(label="Load", custom_id="loadmodule", style=disnake.ButtonStyle.green, emoji=emojis.SwitchNewOnGreen)
    async def loadmodule(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        channel = self.bot.get_channel(interaction.channel_id)
        await interaction.response.send_message('Bitte gebe den Namen des Moduls an, welches du laden möchtest.')

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await channel.send('Du hast zu lange gebraucht, um eine Antwort zu geben.')
        else:
            try:
                self.bot.load_extension(f"{msg.content}")
            except commands.ExtensionAlreadyLoaded:
                await channel.send('Dieses Modul ist bereits geladen.')
            except commands.ExtensionNotFound:
                await channel.send('Dieses Modul konnte nicht gefunden werden.')
            else:
                await channel.send(f'{emojis.Typing} Lade...', delete_after=5)
                await asyncio.sleep(5)
                await channel.send(f'Das Modul {msg.content} wurde erfolgreich geladen.')

    @disnake.ui.button(label="Unload", custom_id="unloadmodule", style=disnake.ButtonStyle.red, emoji=emojis.SwitchNewOff)
    async def unloadmodule(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        channel = self.bot.get_channel(interaction.channel_id)
        await interaction.response.send_message('Bitte gebe den Namen des Moduls an, welches du entladen möchtest.')

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await channel.send('Du hast zu lange gebraucht, um eine Antwort zu geben.')
        else:
            try:
                self.bot.unload_extension(f"{msg.content}")
            except commands.ExtensionNotLoaded:
                await channel.send('Dieses Modul ist bereits entladen.')
            except commands.ExtensionNotFound:
                await channel.send('Dieses Modul konnte nicht gefunden werden.')
            else:
                await channel.send(f'{emojis.Typing} Lade...', delete_after=5)
                await asyncio.sleep(5)
                await channel.send(f'Das Modul {msg.content} wurde erfolgreich entladen.')

    @disnake.ui.button(label="Reload", custom_id="reloadmodule", style=disnake.ButtonStyle.blurple, emoji=emojis.SwitchAndroidOn)
    async def reloadmodule(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        channel = self.bot.get_channel(interaction.channel_id)
        await interaction.response.send_message('Bitte gebe den Namen des Moduls an, welches du neu laden möchtest.')

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await channel.send('Du hast zu lange gebraucht, um eine Antwort zu geben.')
        else:
            try:
                self.bot.reload_extension(f"{msg.content}")
            except commands.ExtensionNotLoaded:
                await channel.send('Dieses Modul ist nicht geladen.')
            except commands.ExtensionNotFound:
                await channel.send('Dieses Modul konnte nicht gefunden werden.')
            else:
                await channel.send(f'{emojis.Typing} Lade...', delete_after=5)
                await asyncio.sleep(5)
                await channel.send(f'Das Modul {msg.content} wurde erfolgreich neu geladen.')

    @disnake.ui.button(label="Close", custom_id="close", style=disnake.ButtonStyle.grey, emoji=emojis.AuditMessageDel)
    async def close(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        channel = self.bot.get_channel(interaction.channel_id)
        await interaction.response.send_message(f'{emojis.Typing} Das Menü wird geschlossen.')
        await asyncio.sleep(5)
        await channel.send(f'{emojis.AuditMessageDel} Das Menü wurde geschlossen.')
        self.stop()


class ModuleMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="modulemenu", description="Öffnet das Modulmenü.")
    async def modulemenu(self, interaction: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title="Modulmenü", description="Hier kannst du Module laden, entladen und neu laden.", color=style.primaryColor)
        for s in self.bot.extensions:
            embed.add_field(name=f"{emojis.SwitchNewOnGreen} {s}", value=f"Status: Geladen", inline=False)
        d1 = self.bot.extensions
        d2 = search_cogs()
        d3 = list(set(d2) - set(d1))
        for s in d3:
            embed.add_field(name=f"{emojis.SwitchNewOff} {s}", value=f"Status: Entladen", inline=False)
        embed.set_footer(text=f"Angefordert von {interaction.author}", icon_url=interaction.author.avatar.url)
        await interaction.response.send_message(embed=embed, view=MenuButtons(self.bot))


def setup(bot):
    bot.add_cog(ModuleMenu(bot))
