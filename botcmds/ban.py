from discord.ext import commands

@commands.command()
async def ban(ctx):
    await ctx.send('`you` will be banned in 5 minutes.')

async def setup(bot):
    await bot.add_command(ban)