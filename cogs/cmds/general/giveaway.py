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
                :param application:
                :param winners:
                :param duration:
                :param prize:
                :param description:
                :param channel:
                :param ctx:
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
        msg = await channel.send(embed=embed, view=giveaway_on())
        await ctx.send(f"Giveaway started in {channel.mention}!", ephemeral=True)
        await asyncio.sleep(tim)

        if application == 1:
            await msg.edit(view=giveaway_appli())
        else:
            await msg.edit(view=giveaway_off())
        users = await msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        if len(users) < winners:
            winners = len(users)
        winner = random.sample(users, winners)
        await channel.send(f"Congratulations {winner}! You won {prize}!", delete_after=delete_time)
        await msg.edit(view=None)
        await asyncio.sleep(delete_time - round(time.time()))
        await msg.delete()

    @giveaway.sub_command(name="end", description="End a giveaway")
    async def giveaway_end(self, ctx, channel: disnake.TextChannel, message_id: int):
        """
                Parameters
                ----------
                channel : The channel where the giveaway is hosted
                message_id : The message ID of the giveaway
                :param message_id:
                :param channel:
                :param ctx:
        """
        msg = await channel.fetch_message(message_id)
        await msg.edit(view=giveaway_off())
        users = await msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        winner = random.choice(users)
        await channel.send(f"Congratulations {winner.mention}! You won the giveaway!", delete_after=604800)
        await msg.edit(view=None)
        await asyncio.sleep(604800)
        await msg.delete()

    @giveaway.sub_command(name="delete", description="Delete a giveaway")
    async def giveaway_delete(self, ctx, channel: disnake.TextChannel, message_id: int):
        """
                Parameters
                ----------
                channel : The channel where the giveaway is hosted
                message_id : The message ID of the giveaway
                :param message_id:
                :param channel:
                :param ctx:
        """
        msg = await channel.fetch_message(message_id)
        await msg.edit(view=giveaway_off())
        await msg.edit(view=None)
        await msg.delete()

    @giveaway.sub_command(name="reroll", description="Reroll a giveaway")
    async def giveaway_reroll(self, ctx, channel: disnake.TextChannel, message_id: int):
        """
                Parameters
                ----------
                channel : The channel where the giveaway is hosted
                message_id : The message ID of the giveaway
                :param message_id:
                :param channel:
                :param ctx:
        """
        msg = await channel.fetch_message(message_id)
        users = await msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        winner = random.choice(users)
        await channel.send(f"Congratulations {winner.mention}! You won the giveaway!", delete_after=604800)
        await msg.edit(view=None)
        await asyncio.sleep(604800)
        await msg.delete()

    @giveaway.sub_command(name="list", description="List all giveaways")
    async def giveaway_list(self, ctx):
        """
                Parameters
                ----------
                ctx :
                :param ctx:
        """
        pass

    @giveaway.sub_command(name="info", description="Get info about a giveaway")
    async def giveaway_info(self, ctx, channel: disnake.TextChannel, message_id: int):
        """
                Parameters
                ----------
                channel : The channel where the giveaway is hosted
                message_id : The message ID of the giveaway
                :param message_id:
                :param channel:
                :param ctx:
        """
        msg = await channel.fetch_message(message_id)
        await ctx.send(f"**Prize:** {msg.embeds[0].title}\n**Description:** {msg.embeds[0].description}\n**Ended:** <t:{round(msg.embeds[0].fields[0].value.timestamp)}:D> (<t:{round(msg.embeds[0].fields[0].value.timestamp)}:R>)\n**Winners:** {msg.embeds[0].fields[1].value}\n**Hosted by:** {msg.embeds[0].fields[2].value}\n**Message ID:** {message_id}", ephemeral=True)


def setup(bot):
    bot.add_cog(Giveaway(bot))
