import discord
import discord_token

client = discord.Client()

@client.event
async def on_message(message : discord.Message):
    if(message.author.bot):
        return

    if(message.content == "/dice"):
        await message.send("ダイス")