from discord.ext import commands
import subprocess

@commands.command()
async def wget(ctx, file, filename):
    if await bot.is_owner(ctx.author):
       subprocess.Popen(['powershell', 'wget', file, '-OutFile', filename])
#       await ctx.send(file=discord.File(filename))

async def setup(bot):
    bot.add_command(wget)
