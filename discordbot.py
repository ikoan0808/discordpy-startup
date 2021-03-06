from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信



@bot.command()
async def ping(ctx):
    await ctx.send('うんこー')
    


# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行


bot.run(token)
