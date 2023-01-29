import sqlite3
import disnake
from disnake.ext import commands
import main as alex

dp = alex.default_prefix

conn_settings = sqlite3.connect('settings.db')
cs = conn_settings.cursor()
cs.execute("CREATE TABLE IF NOT EXISTS settings (guild_id INTEGER, prefix TEXT)")
conn_settings.commit()


class Settings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def prefix(self, inter: disnake.ApplicationCommandInteraction, prefix: str):
        """Setzt den Prefix für den Server"""
        cs.execute("SELECT * FROM settings WHERE guild_id = ?", (inter.guild.id,))
        if cs.fetchone() is None:
            cs.execute("INSERT INTO settings (guild_id, prefix) VALUES (?, ?)", (inter.guild.id, prefix))
            conn_settings.commit()
            await inter.response.send_message(f"Der Prefix wurde auf `{prefix}` gesetzt.")
        else:
            cs.execute("UPDATE settings SET prefix = ? WHERE guild_id = ?", (prefix, inter.guild.id))
            conn_settings.commit()
            await inter.response.send_message(f"Der Prefix wurde auf `{prefix}` gesetzt.")

    @commands.slash_command()
    async def getprefix(self, inter: disnake.ApplicationCommandInteraction):
        """Zeigt den Prefix für den Server"""
        cs.execute("SELECT * FROM settings WHERE guild_id = ?", (inter.guild.id,))
        if cs.fetchone() is None:
            await inter.response.send_message(f"Der Prefix ist `{dp}`")
        else:
            cs.execute("SELECT prefix FROM settings WHERE guild_id = ?", (inter.guild.id,))
            prefix = cs.fetchone()[0]
            await inter.response.send_message(f"Der Prefix ist `{prefix}`")

    @commands.slash_command()
    async def resetprefix(self, inter: disnake.ApplicationCommandInteraction):
        """Setzt den Prefix für den Server auf den Standardwert"""
        cs.execute("SELECT * FROM settings WHERE guild_id = ?", (inter.guild.id,))
        if cs.fetchone() is None:
            await inter.response.send_message(f"Der Prefix ist bereits `{dp}`")
        else:
            cs.execute("DELETE FROM settings WHERE guild_id = ?", (inter.guild.id,))
            conn_settings.commit()
            await inter.response.send_message(f"Der Prefix wurde auf `{dp}` gesetzt.")

            
def setup(bot: commands.Bot):
    bot.add_cog(Settings(bot))
