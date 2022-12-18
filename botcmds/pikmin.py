from discord.ext import commands

@commands.command(description="rock pikmin")
async def pikmin(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/607657189003493376/1053821556624740423/rockPikmin.jpeg')
    
async def setup(bot):
    bot.add_command(pikmin)
