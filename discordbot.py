import discord
import discord_token

Intents = discord.Intents.default()
Intents.members = True
client = discord.Client(intents=Intents)

@client.event
async def on_message(message):
    if(message.author.bot):
        return

    if(message.content == "/dice"):
        await message.send("ダイス")

client.run(discord_token.TOKEN)
