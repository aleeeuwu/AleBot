from discord.ext import commands
import random
import os

@commands.hybrid_command(description='gilbert classic edition')
async def gilbold(ctx):
    lines = open('assets/gilbert.txt').read().splitlines()
    gilbertLine = random.choice(lines)
    await ctx.send(gilbertLine)

async def setup(bot):
    if not os.path.exists("assets/gilbert.txt"):
        print("assets/gilbert.txt not found, gilbold command disabled")
        return
    bot.add_command(gilbold)
