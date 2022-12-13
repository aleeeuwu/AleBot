from discord.ext import commands
import subprocess

@commands.command()
async def dir(ctx):
    if await bot.is_owner(ctx.author):
        command = subprocess.Popen(['cmd', '/c', 'dir', '/b'], stdout=subprocess.PIPE)
        text = command.stdout.read()
        retcode = command.wait()
        await ctx.send(text.decode())

def setup(bot):
    bot.add_command(dir)