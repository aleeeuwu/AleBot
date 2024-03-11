from discord.ext import commands
import json
#from botcmds.gilbonus import bonus_check
import random
import asyncio
import os
import time

# Returns a scoreboard list, optionally for a particular server... type should be "wins" or "attempts" but if we ever make more scoreboards for some weird reason then any scoreboard file name can go here
async def get_scoreboard(type: str, guild_id=None):
    if os.path.exists("scoreboards/" + type + ".json"):
        with open("scoreboards/" + type + ".json", "r") as o:
            scoreboard = json.loads(o.read())
            o.close()
        
        if guild_id is None:
            return scoreboard
        
        guild_id = str(guild_id)
        
        if guild_id in scoreboard:
            return scoreboard[guild_id]
    
    
    return {}

# Returns an int of wins for a user in a server
async def get_points(guild_id, user_id):
    guild_id = str(guild_id)
    user_id = str(user_id)
    
    wins = await get_scoreboard("wins", guild_id)
    
    if user_id in wins:
        return wins[user_id]
    
    return 0

# Sets the amount of points a user has in a server... use with caution...
async def set_points(guild_id, user_id, value: int):
    guild_id = str(guild_id)
    user_id = str(user_id)
    
    wins = await get_scoreboard("wins")
    
    if guild_id not in wins:
        wins[guild_id] = {}
    
    wins[guild_id][user_id] = value
    
    with open("scoreboards/wins.json", "w") as o:
        o.write(json.dumps(wins, indent=4))
        o.close()

# Adds a point for a user in a server... really just a convenience for not typing the big long set_points/get_points call shown below...
async def add_points(guild_id, user_id, value: int=1):
    await set_points(guild_id, user_id, await get_points(guild_id, user_id)+value)

# Returns an int of attempts for a user in a server
async def get_attempts(guild_id, user_id):
    guild_id = str(guild_id)
    user_id = str(user_id)
    
    attempts = await get_scoreboard("attempts", guild_id)
    
    if user_id in attempts:
        return attempts[user_id]
    
    return 0

# Adds an attempt for a user in a server... unlikely to ever add more than 1, but who knows...
async def add_attempts(guild_id, user_id, value: int=1):
    guild_id = str(guild_id)
    user_id = str(user_id)
    
    attempts = await get_scoreboard("attempts")
    
    if guild_id not in attempts:
        attempts[guild_id] = {}
    
    attempts[guild_id][user_id] = await get_attempts(guild_id, user_id)+value
    
    with open("scoreboards/attempts.json", "w") as o:
        o.write(json.dumps(attempts, indent=4))
        o.close()

@commands.hybrid_command(description='gilbert')
async def gilbert(ctx, *, guess=None):
    # if not names_loaded:
        # await ctx.send("Command currently disabled because the names aren't loaded yet")
        # return
        
        # really dumb, need to do this because I can't get the user's name before the bot logs on
        #if not names_list:
        #    for userid in tries_list:
        #        current_user = await foobot.fetch_user(userid)
        #        names_list[userid] = current_user.name
    
    
    #picks random bert
    random_gilbert = random.choice(list(gilbert_list.keys()))
    
    #list of values of the random bert in lowercase
    value_gilbert = [item.lower() for item in gilbert_list[random_gilbert]]
    
    #hope
    user_id = str(ctx.author.id)
    
    #sends random bert
    await ctx.send(random_gilbert)
    
    #exception if no guess
    if guess is None:
        return
    
    if user_id not in names_list:
        names_list[user_id] = ctx.author.name
    
    #first checks to see if the user has played or not before, and if not, adds it to the user list
    if not user_id in (users_list.keys()):
        users_list[user_id] = 1
        
        json_object = json.dumps(users_list, indent=4)
        with open("assets/users.json", "w") as o:
            o.write(json_object)
            o.close()
    
    #sends a message if it was correct or not
    if guess.lower() in value_gilbert:
        await ctx.send('Congratulations, ' + ctx.author.mention + '!' + ' You are the Godbert, you got 1 Gilpoint!')
        
        #if user exists they get one point...
        await add_points(ctx.guild.id, ctx.author.id)
    
    #in case of catastrophic failure:
    else:
        await ctx.send('Tough luck!')
    
    # update attempts scores
    await add_attempts(ctx.guild.id, ctx.author.id)

async def setup(bot):
    global foobot
    foobot = bot
    global gilbert_list
    if os.path.exists("assets/Gilberts.json"):
        with open("assets/Gilberts.json", "r") as o:
            gilbert_list = json.loads(o.read())
            o.close()
        bot.add_command(gilbert)
    else:
        print("assets/Gilberts.json not found, gilbert command disabled")
        return
    
    global users_list
    if os.path.exists("assets/users.json"):
        with open("assets/users.json", "r") as o:
            users_list = json.loads(o.read())
            o.close()
    else:
        users_list = {}
        json_object = json.dumps(users_list, indent=4)
        with open("assets/users.json", "w") as o:
            o.write(json_object)
            o.close()
    
    if not os.path.isdir("scoreboards"):
        os.makedirs("scoreboards")
    
    # print("getting scoreboard names")
    
    # global names_loaded 
    # names_loaded = False
    
    # global names_list
    # names_list = {}
    
    # for userid in users_list:
        # current_user = await bot.fetch_user(userid)
        # names_list[userid] = current_user.name
    # names_loaded = True
    
    # print("names stored")