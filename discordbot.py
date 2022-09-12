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
    if(message.author.bot):
        return
    if(message.content[0]  != "/"):
        return

    if("/dice" in message.content):
        try:
            text = message.content[6:]
            texts = text.split("d")
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
            print("=== エラー内容 ===")
            print("type:" + str(type(e)))
            print('args:' + str(e.args))
            print('message:' + e.message)
            print('e自身:' + str(e))
    else:
            await message.reply("コマンドが不正です")

client.run(discord_token.TOKEN)