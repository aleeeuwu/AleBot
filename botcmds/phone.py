from discord.ext import commands

@commands.group()
async def phone(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('you have to specify something dummy')

@phone.command()
async def start(ctx, phonechannelid2: int):
    if await bot.is_owner(ctx.author):
        global textphone
        global first_phone_channel
        global second_phone_channel
        textphone = True
        first_phone_channel = int(ctx.channel.id)
        second_phone_channel = int(phonechannelid2)
        await ctx.send('Phone started')
        #await bot.fetch_channel(second_phone_channel).send('Incoming call! Say hello!')
        print(first_phone_channel)
        print(second_phone_channel)
        print(textphone)

@phone.command()
async def stop(ctx):
    if await bot.is_owner(ctx.author):
        global textphone
        global first_phone_channel
        global second_phone_channel
        textphone = False
        first_phone_channel = 0
        second_phone_channel = 0
        await ctx.send('Phone stopped')

async def setup(bot):
    bot.add_command(phone)
