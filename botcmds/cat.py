from discord.ext import commands
import catapi
import random
import configparser
import os


@commands.hybrid_command(description='sends a random cat, has a 10% chance of sending a dumbass cat instead')
async def cat(ctx):
    cat = await apimeow.search_images(limit=1)
    chance = random.randint(1, 10)
    if chance == 10:
        await ctx.send("https://cdn.discordapp.com/attachments/607673609074376876/824823278840578058/IMG_1641.JPG")
    else:
        await ctx.send(cat[0].url)

async def setup(bot):
    config = configparser.ConfigParser()
    config.read('aleconfig.ini')
    try:
        token = config['Main']['catapi_token']
    except:
        print("cat api token not found, command disabled")
        return


    global apimeow
    apimeow = catapi.CatApi(api_key=token)
    bot.add_command(cat)
