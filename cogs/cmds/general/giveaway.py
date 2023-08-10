import asyncio
import random
import time
import disnake
from disnake import ButtonStyle
from disnake.ext import commands


class giveaway_on(disnake.ui.View):
    def __init__(self):
        super().__init__()

    @disnake.ui.button(style=ButtonStyle.grey,
                       custom_id="giveaway_on",
                       emoji='<a:tada_new:998560941673300048>')
    async def give_on(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass


class giveaway_appli(disnake.ui.View):
    def __init__(self):
        super().__init__()

    @disnake.ui.button(style=ButtonStyle.grey, custom_id='giveaway_appli',
                       emoji='<a:tada_new:998560941673300048>')  ### Emoji von oben ergänzen
    async def give_appli(self, button, interaction):
        pass


class giveaway_off(disnake.ui.View):
    def __init__(self):
        super().__init__()

    @disnake.ui.button(style=ButtonStyle.grey,
                       custom_id="giveaway_off",
                       emoji='<a:tada_new:998560941673300048>', disabled=True)
    async def give_off(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        pass


class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    # self.on_giveaway_end.start()
    # self.on_giveaway_delete.start()

    @commands.slash_command(name="giveaway")
    async def giveaway(self, ctx):
        pass

    art = commands.option_enum(choices={'Yes': 1, 'No': 0})

    @giveaway.sub_command(name="start", description="Start a giveaway")
    async def giveaway_start(self, ctx, channel: disnake.TextChannel, description: str, prize: str, duration: str,
                             winners: int, application: art):
        """
                Parameters
                ----------
                channel : The channel where the giveaway should be hosted
                description : The description of the giveaway
                prize : The prize of the giveaway
                duration : The duration of the giveaway
                winners : The amount of winners
        """
        unit = duration[-1]
        if unit == 's':
            tim = int(duration[:-1])
        elif unit == 'm':
            tim = int(duration[:-1]) * 60
        elif unit == 'h':
            tim = int(duration[:-1]) * 60 * 60
        elif unit == 'd':
            tim = int(duration[:-1]) * 60 * 60 * 24
        elif unit == 'w':
            tim = int(duration[:-1]) * 60 * 60 * 24 * 7
        else:
            return await ctx.send('Invalid unit! Use `s`, `m`, `h`, `d` or `w`.',
                                  ephemeral=True)  # Invalid unit! Use `s`, `m`, or `h`.
        if winners < 1:
            return await ctx.send('You need at least one winner!', ephemeral=True)
        delete_time = 604800  # 7 days

        giveaway_id = round(time.time())
        ti = round(time.time())
        delete_time = round(time.time()) + tim + delete_time
        embed = disnake.Embed(title=f'{prize}', description=f'{description}', colour=ctx.author.colour)
        embed.add_field(name='Ended:', value=f'<t:{round(ti + tim)}:D> (<t:{round(ti + tim)}:R>)', inline=False)
        embed.add_field(name='Winners:', value=f'{winners}', inline=False)
        embed.add_field(name='Hosted by:', value=f'{ctx.author.mention}', inline=False)
        embed.set_footer(text=f"Giveway ID: {giveaway_id}")

    if art == 0:
        msg = await ctx.channel.send(embed=embed, view=giveaway_on())
    elif art == 1:
        msg = await ctx.channel.send(embed=embed, view=giveaway_appli())
