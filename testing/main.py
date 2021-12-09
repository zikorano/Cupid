from types import MemberDescriptorType
from discord import Client
import discord
from discord.message import Message
from config import ConfigManager

cm = ConfigManager()
client = Client()

@client.event
async def on_ready():
    login_message = f"{client.user} has logged in successfully."
    print(login_message)

@client.event
async def on_message(message: Message):
    print(f"{message.author}: {message.content}")

if __name__ == "__main__":
    clientToken = cm.credentials["clientToken"]
    client.run(clientToken)