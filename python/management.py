from discord.ext import commands
import discord
import asyncio

intents = discord.Intents.all()
TOKEN = 'NjUwMDE1MzE5NDg1NTc5Mjc1.XfZX-w.eNAaAKWjHsF8-qHDqR7DiLkshrg' #TOKENを入力してください
prefix = "/" #お好きなプレフィックス

bot = commands.Bot(command_prefix=prefix,help_command=None,intents=intents)

bot.load_extension("Cogs.default")
bot.load_extension("voiceChannelJoinLeave_roleModify")

bot.run(TOKEN)