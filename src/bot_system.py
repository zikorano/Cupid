from discord.ext import commands
from discord import Message
import discord, json

configFile = open("config/config.json", "r")
config = json.load(configFile)
token = config["ClientToken"]

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
	print(f"{bot.user.name} has connected to Discord succesfully!")

@bot.command()
async def register(ctx):
	await ctx.send("logging you into the database...")

@bot.event
async def on_message(message: Message):
	channel = message.channel
	if message.author == bot.user:
		return
	if message.content == "Woo":
		await channel.send("Woo right back at ya!")


if __name__ == "__main__":
	configFile.close()
	bot.run(token)
