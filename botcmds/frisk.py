from discord.ext import commands
import random

@commands.command(description='Random frisk video courtesy of I Like Pancakes#1515')
async def frisk(ctx):
    lines = open('frisk.txt').read().splitlines()
    myline = random.choice(lines)
    await ctx.send(myline)

async def setup(bot):
    bot.add_command(frisk)
