import discord
from discord.ext import commands
import random

@commands.command(description="Sends a random Mokou image. Artist is @jokanhiyou on Twitter.")
async def mokou(ctx):
    mokouNumber = random.randint(1, 700)
    await ctx.send(str(mokouNumber), file=discord.File('mokou/' + str(mokouNumber) + '.jpg'))

def setup(bot):
    bot.add_command(mokou)
