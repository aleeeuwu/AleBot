from discord.ext import commands
import time

@commands.command()
async def ban(ctx):
    theTime = int(time.time()) + 300
    await ctx.send('`you` will be banned in <t:' + theTime + ':R>.')

async def setup(bot):
    bot.add_command(ban)
