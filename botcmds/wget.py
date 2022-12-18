from discord.ext import commands
import subprocess
from botcmds.privilege import adminCheck

@commands.hybrid_command()
async def wget(ctx, file, filename):
    if adminCheck(ctx.author.id):
       subprocess.Popen(['powershell', 'wget', file, '-OutFile', filename])
#       await ctx.send(file=discord.File(filename))
    else:
        await ctx.send('You need privileges to use this command!')

async def setup(bot):
    bot.add_command(wget)
