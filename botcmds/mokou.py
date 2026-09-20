import discord
from discord.ext import commands
import random
import os
import configparser

@commands.hybrid_command(description="Sends a random Mokou image. Artist is @jokanhiyou on Twitter.")
async def mokou(ctx):
    mokou_number = random.randint(1, mokou_images)
    await ctx.send(str(mokou_number), file=discord.File('assets/mokou/' + str(mokou_number) + '.jpg'))

async def setup(bot):
    if not os.path.isdir("assets/mokou/"):
        print("assets/mokou/ not found, command disabled")
        return

    config = configparser.ConfigParser()
    config.read('aleconfig.ini')
    try:
        global mokou_images
        mokou_images = int(config['Main']['mokou_images'])
    except:
        print("failed to load mokou_images variable, command disabled")
        return

    bot.add_command(mokou)
