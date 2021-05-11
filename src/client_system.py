from discord import Client, Message

client = Client()

@client.event
async def on_message(message: Message):
    pass
