import discord
from discord.ext import commands
import time
import json
import os
from botcmds.gilbert import get_points, add_points

async def bonus_check(guild_id: int, user_id: int):
    if guild_id in bonuses:
        if int(time.time()) - bonuses[guild_id][user_id] < 1800:
            return True
    return False

@commands.hybrid_command(description='Activate the Gilbert multiplier to temporarily double your points earned from a guess!')
async def gilbonus(ctx):
    class Confirm(discord.ui.View):
        @discord.ui.button(label='Activate', style=discord.ButtonStyle.green)
        async def confirm(self, interaction, button):
            if interaction.user.id == ctx.author.id:
                if await get_points(ctx.guild.id, ctx.author.id) >= 5:
                    await add_points(ctx.guild.id, ctx.author.id, -5)
                    
                    if ctx.guild.id not in bonuses:
                        bonuses[ctx.guild.id] = {}
                    bonuses[ctx.guild.id][ctx.author.id] = int(time.time())
                    
                    await interaction.response.send_message(interaction.user.display_name + ' has activated their Gilbert score multiplier!', ephemeral=False)
                    
                    self.value = True
                    self.stop() 
    
    #Checks the score of the user
    if await get_points(ctx.guild.id, ctx.author.id) < 5:
        await ctx.send("You don't seem to have enough gilpoints")
        return
    
    view = Confirm()
    
    await ctx.send('Do you want to activate your Gilbert score multiplier in this server?', view=view, ephemeral=True)
    
    # Wait for the View to stop listening for input...
    await view.wait()
    
    # If the button was pressed...
    if view.value:
        if ctx.guild.id not in bonuses.keys():
            bonuses[ctx.guild.id] = {}
        bonuses[ctx.guild.id][ctx.author.id] = int(time.time())
        
        print('[' + time.asctime() + ']', 'User ID', ctx.author.id, 'in guild ID', ctx.guild.id, 'activated Gilbert multiplier.')

async def setup(bot):
    bot.add_command(gilbonus)
    global bonuses
    bonuses = {}