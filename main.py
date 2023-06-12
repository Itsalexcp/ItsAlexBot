import os
from disnake.flags import Intents
from disnake.ext import commands
import disnake

from cogs.events.Client.ready import status_task


# bot instance
class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop.create_task(status_task())


# commands sync
command_sync_flags = commands.CommandSyncFlags.default()

# Bot Instance
bot = commands.Bot(
    intents=Intents.all(),
    case_insensitive=False,
    test_guilds=[673481402448085024],
    command_sync_flags=command_sync_flags,
    description="ItsAlex Enterprise - Ein völlig neuer Bot der auf Disnake basiert.",
    owner_id=494959967774834694,
    reload=True,
)


def load_cogs():
    for folder, subfolder, file in os.walk("cogs/"):
        for filename in file:
            if filename.endswith(".py"):
                filenamepath = os.path.join(folder, filename)
                filenamepath = filenamepath.replace("\\", ".")
                filenamepath = filenamepath.replace("/", ".")
                filenamepath = filenamepath.replace(".py", "")
                bot.load_extension(filenamepath)


load_cogs()

# push to github
bot.run(os.environ.get("TOKEN"))
# test

