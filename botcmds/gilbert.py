from discord.ext import commands
import json
import random
import asyncio
import os
import time

@commands.hybrid_command(description='gilbert')
async def gilbert(ctx, *, guess=None):
    if not names_loaded:
        await ctx.send("Command currently disabled because the names aren't loaded yet")
        return

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
    user_id = ctx.author.id

    #sends random bert
    await ctx.send(random_gilbert)

    #exception if no guess
    if guess is None:
        return

    if user_id not in names_list:
        current_user = await foobot.fetch_user(user_id)
        names_list[user_id] = current_user.name

    #first checks to see if the user has played or not before, and if not, adds it to the user list
    if not str(user_id) in (users_list.keys()):
        users_list[user_id] = 1

        json_object = json.dumps(users_list, indent=4)
        with open("assets/users.json", "w") as o:
            o.write(json_object)
            o.close()

    #sends a message if it was correct or not
    if guess.lower() in value_gilbert:
        await ctx.send('Congratulations, ' + ctx.author.mention + '!' + ' You are the Godbert, you got 1 Gilpoint!')

        #reads the scoreboard file for the server
        if os.path.exists("scoreboards/wins/" + str(ctx.guild.id) + ".json"):
            with open("scoreboards/wins/" + str(ctx.guild.id) + ".json", "r") as o:
                wins = json.loads(o.read())
                o.close()

        #check if the scoreboard file for the server exists, if not, makes it
        else:
            wins = {}
            json_object = json.dumps(wins, indent=4)
            with open("scoreboards/wins/" + str(ctx.guild.id) + ".json", "w") as o:
                o.write(json_object)
                o.close()

        #if user exists they get one point...
        if str(user_id) in (wins.keys()):
            wins[str(user_id)] += 1

        #and if they don't, they get added
        else:
            wins[str(user_id)] = 1
        
        #finally it writes the score to the file
        json_object = json.dumps(wins, indent=4)
        with open("scoreboards/wins/" + str(ctx.guild.id) + ".json", "w") as o:
            o.write(json_object)
            o.close()

    #in case of catastrophic failure:
    else:
        await ctx.send('Tough luck!')

    # update attempts scores
    #read the scoreboard file for the server
    if os.path.exists("scoreboards/attempts/" + str(ctx.guild.id) + ".json"):
        with open("scoreboards/attempts/" + str(ctx.guild.id) + ".json", "r") as o:
            attempts = json.loads(o.read())
            o.close()

    #check if the scoreboard file for the server exists, if not, makes it
    else:
        attempts = {}
        json_object = json.dumps(attempts, indent=4)
        with open("scoreboards/attempts/" + str(ctx.guild.id) + ".json", "w") as o:
            o.write(json_object)
            o.close()

    if str(user_id) in (attempts.keys()):
        attempts[str(user_id)] += 1

    else:
        attempts[str(user_id)] = 1
    
    json_object = json.dumps(attempts, indent=4)
    with open("scoreboards/attempts/" + str(ctx.guild.id) + ".json", "w") as o:
         o.write(json_object)
         o.close()

async def get_names():
    print("getting scoreboard names")
    # have to import THIS FILE because of weird python and asyncio shenanigans lmao
    import botcmds.gilbert as g
    if not names_list:
        for userid in users_list:
            current_user = await foobot.fetch_user(userid)
            names_list[userid] = current_user.name
    g.names_loaded = True
    print("names stored")


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
    
    if not os.path.isdir("scoreboards/wins"):
        os.makedirs("scoreboards/wins")

    if not os.path.isdir("scoreboards/attempts"):
        os.makedirs("scoreboards/attempts")

    global names_list
    names_list = {}
    global names_loaded 
    names_loaded = False
    asyncio.ensure_future(get_names())
