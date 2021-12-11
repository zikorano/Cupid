from discord.ext import commands
from ...config import ConfigManager
import _commands as cmds

cm = ConfigManager()
bot = commands.Bot(
    description    = cm.botAttrs["description"],
    command_prefix = cm.botAttrs["commandPrefix"]
)

bot.add_command(cmds.signup)
bot.add_command(cmds.profile)
