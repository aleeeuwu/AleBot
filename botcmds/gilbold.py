from discord.ext import commands
import random

@commands.hybrid_command(description='gilbert classic edition')
async def gilbold(ctx):
    lines = open('gilbert.txt').read().splitlines()
    gilbertLine = random.choice(lines)
    await ctx.send(gilbertLine)

async def setup(bot):
    bot.add_command(gilbold)
