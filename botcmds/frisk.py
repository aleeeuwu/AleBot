from discord.ext import commands
import random
import os

@commands.hybrid_command(description='Random frisk video courtesy of I Like Pancakes#1515')
async def frisk(ctx):
    lines = open('frisk.txt').read().splitlines()
    myline = random.choice(lines)
    await ctx.send(myline)

async def setup(bot):
    if not os.path.exists("frisk.txt"):
        print("frisk file not found, command disabled")
        return
    bot.add_command(frisk)
