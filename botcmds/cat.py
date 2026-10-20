from discord.ext import commands
import requests
import random
import configparser
import os


@commands.hybrid_command(description='sends a random cat, has a 10% chance of sending a dumbass cat instead')
async def cat(ctx):
    global last_result_error

    chance = random.randint(1, 10)

    if chance != 10 or last_result_error:
        try:
            cat = requests.get("https://api.thecatapi.com/v1/images/search?limit=1", headers={"x-api-key": token}, timeout=5)
            cat.raise_for_status()
        except Exception as e:
            last_result_error = True
            print("error in cat command:", e)
            await ctx.send("Meowthing went wrong. Check your console for details.")
            return

        cat_url = cat.json()[0]['url']
        await ctx.send(cat_url)

        last_result_error = False
    else:
        await ctx.send("https://cdn.discordapp.com/attachments/607673609074376876/824823278840578058/IMG_1641.JPG")

async def setup(bot):
    config = configparser.ConfigParser()
    config.read('aleconfig.ini')
    try:
        global token
        token = config['Main']['catapi_token']
    except:
        print("cat api token not found, command disabled")
        return

    global last_result_error
    last_result_error = False

    bot.add_command(cat)
