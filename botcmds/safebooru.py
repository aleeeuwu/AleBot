from discord.ext import commands
from pybooru import Danbooru

dansafe = Danbooru('safebooru')

@commands.hybrid_command(description='Sends a random post from safebooru.')
async def safebooru(ctx, arg):
    if ctx.channel.id == 0:
        tags = arg
        post = dansafe.post_list(tags=tags, limit=1, random=True)
        for post in post:
            await ctx.send("Image path: {0}".format(post['file_url']))

async def setup(bot):
    bot.add_command(safebooru)
