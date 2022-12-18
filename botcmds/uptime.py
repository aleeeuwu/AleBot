import discord
from discord.ext import commands

import time

@commands.hybrid_command()
async def uptime(ctx):
    currTime = time.time()
    # should probably make it says hours and days and whatever instead
    await ctx.send("It has been " + str(round(currTime - startTime)) + " seconds since startup (or reload)")

async def setup(bot):
    bot.add_command(uptime)
    # this always happens when reloaded, probably should fix that but idk
    global startTime
    startTime = time.time()
