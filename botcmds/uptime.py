import discord
from discord.ext import commands

import time
from math import floor

# to reduce repeated code
def getTimeUnits(seconds, divisor, modulus, unitString):
    string = ""
    units = 0
    if modulus != -1:
        if seconds/divisor % modulus < 1:
            return ""
        if seconds/divisor > modulus:
            string += ", "
        units = floor(seconds/divisor % modulus)
    else:
        # just for days so it doesn't put , before them
        if seconds/divisor < 1:
            return ""
        units = floor(seconds/divisor)

    string += str(units) + " " + unitString
    if units > 1:
        string += "s"
    return string

@commands.hybrid_command()
async def uptime(ctx):
    seconds = time.time() - startTime
    # there's probably some random python module that does this but I don't care enough to read through all of pythons docs right now
    timeStr = ""
    timeStr += getTimeUnits(seconds, 60*60*24, -1, "day")
    timeStr += getTimeUnits(seconds, 60*60, 24, "hour")
    timeStr += getTimeUnits(seconds, 60, 60, "minute")
    if seconds > 60:
        timeStr += " and "
    timeStr += str(floor(seconds%60)) 
    if floor(seconds%60) == 1:
        timeStr += " second"
    else:
        timeStr += " seconds"
    await ctx.send("It has been " + timeStr + " since startup (or reload)")

async def setup(bot):
    bot.add_command(uptime)
    # this always happens when reloaded, probably should fix that but idk
    global startTime
    startTime = time.time()
