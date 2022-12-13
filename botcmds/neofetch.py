from discord.ext import commands
import subprocess

@commands.command()
async def neofetch(ctx):
    p = subprocess.Popen(['bash', 'neofetch', '--stdout'], stdout=subprocess.PIPE)
    text = p.stdout.read()
    retcode = p.wait()
    await ctx.send(text.decode())

async def setup(bot):
    bot.add_command(neofetch)
