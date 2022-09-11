import discord
from discord.ext import commands
from dislash import slash_commands, Option, OptionType

import discord_token

import random

Intents = discord.Intents.default()
Intents.message_content = True
Intents.messages = True
Intents.guild_messages = True
client = discord.Client(intents=Intents)

@slash_commands(
    name="DICE☆KE",
    description = "ダイスを振るよ！",
    options = [Option("text", "ダイスを指定してね", OptionType.STRING)]
)
async def dice(inter, text:str=None):
    if text is not None:
        try:
            texts = text.split("d")
            roll_time = int(texts[0])
            face_num = int(texts[1])
            result:str = None

            if roll_time == 1:
                result = str(random.randint(0,  face_num))
            elif roll_time > 1:
                # for i in range(roll_time):
            # else:
                # raise Exception
        # except:
            # await inter.reply("ダイスの値が不正です")


# @client.event
# async def on_message(message : discord.message.Message):
#     if(message.author.bot):
#         return

#     if(message.content == "/dice"):
#         await message.channel.send("ダイス")

client.run(discord_token.TOKEN)
