from discord.ext import commands
from config import ConfigManager

cm = ConfigManager()
bot = commands.Bot(
    description    = cm.attrs["description"],
    help_command   = cm.attrs["helpCommand"],
    command_prefix = cm.attrs["commandPrefix"]
)


