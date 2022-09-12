import discord
import discord_token
import random

Intents = discord.Intents.default()
Intents.message_content = True
Intents.messages = True
Intents.guild_messages = True
client = discord.Client(intents=Intents)

@client.event
async def on_message(message : discord.message.Message):
    content = message.content
    content = content.replace(" ", "")
    if(message.author.bot or content[0]  != "/"):
        return

    try:
        texts = content.split("/")[1].split("d")
        roll_time = int(texts[0])
        face_num = int(texts[1])
        dice_nums = []
        total_num:int = 0

        if roll_time == 1:
            num = random.randint(0,  face_num)
            dice_nums.append(num)
            total_num = num
        elif roll_time > 1:
            for i in range(roll_time):
                num = random.randint(0,  face_num)
                dice_nums.append(num)
                total_num += num
        else:
            raise Exception
        await message.reply(f"{total_num} {dice_nums}")
    except Exception as e:
        await message.reply("ダイスの値が不正です")
        await message.reply(f"===エラー内容===\n type:{type(e)}\n args:{e.args}\n message:{e.message}\n error:{e}")
client.run(discord_token.TOKEN)