import discord
from discord.ext import commands
import random
from botcmds.privilege import adminCheck
import time

@commands.hybrid_command(description='Hello!')
async def hello(ctx):
    await ctx.send('Hello!')

@commands.hybrid_command(description='what kind of description am I supposed to put for this')
async def fuck(ctx):
    await ctx.send('fuck TWO')

@commands.hybrid_command(description='sends the REDDIT image')
async def reddit(ctx):
    await ctx.send(file=discord.File('REDDIT.png'))
    
@commands.hybrid_command(description="rock pikmin")
async def pikmin(ctx):
    embedPikmin = discord.Embed(title='Rock Pikmin', color=None)
    embedPikmin.set_image(url='https://cdn.discordapp.com/attachments/607657189003493376/1053821556624740423/rockPikmin.jpeg')
    await ctx.send(embed=embedPikmin)

@commands.hybrid_command(description='you will recieve a nice message')
async def textme(ctx):
    await ctx.author.send('hello bitch')

#echoes a sent message
@commands.hybrid_command(description='echoes a sent message')
async def echo(ctx, *, arg):
    await ctx.send(arg)

#shows the bot's latency
@commands.hybrid_command(description='shows the bot\'s latency')
async def ping(ctx):
    await ctx.send(f'Funny ping is {foobot.latency * 1000}ms')

#luigi sends the bot's latency as an integer
@commands.hybrid_command(description='luigi sends the bot\'s latency as an integer')
async def luigiping(ctx):
    await ctx.send(f'Mama mia! The-a ping is {round(foobot.latency * 1000)}ms!')
    await ctx.send('https://cdn.discordapp.com/attachments/806576196388913232/806576253536174161/MP3_Luigi_Artwork.png')

#picks a random number between the specified numbers
@commands.hybrid_command(description='picks a random number between the specified numbers')
async def rng(ctx,arg: int,arg2: int):
    random.randint(arg, arg2)
    await ctx.send(random.randint(arg, arg2))

#the legendary and awful hug command.
@commands.hybrid_command(description='the legendary and awful hug command.')
async def hug(ctx,*,arg):
    await ctx.send(f'<@{ctx.author.id}> hugged {arg}!')

@commands.hybrid_command()
async def ban(ctx):
    theTime = int(time.time()) + 300
    await ctx.send('`you` will be banned <t:' + str(theTime) + ':R>.')

@commands.hybrid_command(description='heads or tails')
async def coinflip(ctx):
    num = random.randint(1, 2)
    if num == 1:
        await ctx.send('Heads')
    elif num == 2:
        await ctx.send('Tails')

@commands.hybrid_group(description='add, subtract, multiply, or divide two numbers')
async def math(ctx):
    if ctx.invoked_subcommand is None:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        await ctx.send(f'{a} + {b} = {a + b}')

@math.command()
async def add(ctx, a: int, b: int):
    if a == 9:
        if b == 10:
            await ctx.send('21')
            await ctx.send('https://tenor.com/view/vine-21-whats-nine-plus-ten-twenty-one-gif-20252658')
            return
    await ctx.send(a + b)

@math.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send(a - b)

@math.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)

@math.command()
async def divide(ctx, a: int, b: int):
    await ctx.send(a / b)

@commands.hybrid_command()
async def dm(ctx, user: discord.User, *, message):
    if adminCheck(ctx.author.id):
        await user.send(message)
        print(ctx.author, user, message)
    else:
        await ctx.send('You need privileges to use this command!')

@commands.hybrid_command()
async def avatar(ctx, user: discord.User):
    await ctx.send(user.avatar_url)

async def setup(bot):
    bot.add_command(hello)
    bot.add_command(fuck)
    bot.add_command(reddit)
    bot.add_command(pikmin)
    bot.add_command(textme)
    bot.add_command(echo)
    bot.add_command(ping)
    bot.add_command(luigiping)
    bot.add_command(rng)
    bot.add_command(hug)
    bot.add_command(ban)
    bot.add_command(coinflip)
    bot.add_command(math)
    bot.add_command(dm)
    bot.add_command(avatar)
    global foobot
    foobot = bot
