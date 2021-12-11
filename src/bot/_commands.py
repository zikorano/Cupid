from discord.ext.commands.context import Context
from discord.ext import commands
import _actions

@commands.command()
async def signup(ctx: Context, arg):
    _actions.createNewUserProfile(ctx.author, arg)

@commands.command()
async def profile(ctx: Context, *args):
    """
    Command for modifying the user's profile data

    Usage: `$profile <attribute> <value>`
    
    Where `attribute` is a field in the user's profile and `value`
    is a new value to be assigned to that field

    Displays the user's profile as an embed if no arguments are passes
    """
    if len(args) == 0:
        _actions.sendUserProfileEmbed(ctx.author, ctx.channel)
    elif len(args) == 2: 
        attr, value = args
        _actions.updateUserProfileData(ctx.author, attr, value)