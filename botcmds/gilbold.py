from discord.ext import commands
import random
import os

@commands.hybrid_command(description='gilbert classic edition')
async def gilbold(ctx):
    lines = open('gilbert.txt').read().splitlines()
    gilbertLine = random.choice(lines)
    await ctx.send(gilbertLine)

async def setup(bot):
    if not os.path.exists("gilbert.txt"):
        print("gilbert.txt file (not the main one) not found, gilbold command disabled")
        return
    bot.add_command(gilbold)
