from discord.ext import commands
import subprocess
from botcmds.privilege import adminCheck

@commands.command()
async def dir(ctx):
    if adminCheck(ctx.author.id):
        command = subprocess.Popen(['cmd', '/c', 'dir', '/b'], stdout=subprocess.PIPE)
        text = command.stdout.read()
        retcode = command.wait()
        await ctx.send(text.decode())
    else:
        await ctx.send('You need privileges to use this command!')

async def setup(bot):
    bot.add_command(dir)
