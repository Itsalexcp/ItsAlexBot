import disnake
from disnake.ext import commands
import defaults
from defaults import emojis
from defaults import channels
from defaults import style
from disnake import TextInputStyle
import disnake.ui


class SuggestModal(disnake.ui.Modal):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label="Name",
                placeholder="Schreibe hier deinen Namen",
                style=TextInputStyle.short,
                custom_id="Name",
                min_length=1,
                max_length=1000,
                required=True,
            ),
            disnake.ui.TextInput(
                label="Vorschlag",
                placeholder="Schreibe hier deinen Vorschlag",
                style=TextInputStyle.long,
                custom_id="Vorschlag",
                min_length=1,
                max_length=1000,
                required=True,
            ),
            disnake.ui.TextInput(
                label="Umsetzung",
                placeholder="Schreibe hier deine Umsetzung",
                style=TextInputStyle.long,
                custom_id="Umsetzung",
                min_length=0,
                max_length=1000,
                required=False,
            ),
        ]
        super().__init__(title="Vorschlag", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title=f"Ein neuer Vorschlag von {inter.author.name}#{inter.author.discriminator}",)
        embed.add_field(name="Danke", value=inter.author.mention, inline=False)
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        await self.bot.get_channel(channels.suggestions).send(embed=embed)
        await inter.response.send_message("Dein Vorschlag wurde gesendet!", ephemeral=True)
        await inter.response.edit_message(embed=embed, view=None)


class Suggestion(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name="suggest",
        description="Schreibe einen Vorschlag für den Server",

    )
    async def suggest(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_modal(SuggestModal(bot=self.bot))


def setup(bot: commands.Bot):
    bot.add_cog(Suggestion(bot))




