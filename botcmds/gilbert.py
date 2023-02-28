from discord.ext import commands
import json
import random
import asyncio
import os

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

    #sends a message if it was correct or not
    if guess.lower() in value_gilbert:
        await ctx.send('Congratulations, ' + ctx.author.mention + '!' + ' You are the Godbert, you got 1 Gilpoint!')

        #to open a file to read
        #with open("assets/scores.json", "r") as o:
        #    scores = json.loads(o.read())

        #if user exists they get one point...
        if str(user_id) in (scores_list.keys()):
            scores_list[str(user_id)] += 1

        #and if they don't, they get added
        else:
            scores_list[str(user_id)] = 1
        
        #finally it writes the score to the file
        json_object = json.dumps(scores_list, indent=4)
        with open("assets/scores.json", "w") as o:
            o.write(json_object)

        #now for the tries:
        #with open("assets/tries.json", "r") as o:
        #    tries = json.loads(o.read())

        if str(user_id) in (tries_list.keys()):
            tries_list[str(user_id)] += 1

        else:
            tries_list[user_id] = 1
        
        json_object = json.dumps(tries_list, indent=4)
        with open("assets/tries.json", "w") as o:
            o.write(json_object)

    #in case of catastrophic failure:
    else:
        await ctx.send('Tough luck!')
        #with open("assets/tries.json", "r") as o:
        #    tries = json.loads(o.read())

        if str(user_id) in (tries_list.keys()):
            tries_list[str(user_id)] += 1

        else:
            tries_list[str(user_id)] = 1
        
        json_object = json.dumps(tries_list, indent=4)
        with open("assets/tries.json", "w") as o:
            o.write(json_object)

async def get_names():
    print("getting scoreboard names")
    # have to import THIS FILE because of weird python and asyncio shenanigans lmao
    import botcmds.gilbert as g
    if not names_list:
        for userid in tries_list:
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
        bot.add_command(gilbert)
    else:
        print("assets/Gilberts.json not found, gilbert command disabled")
    # different name so that importing it in scoreboard.py doesn't make it import the function
    global tries_list
    if os.path.exists("assets/tries.json"):
        with open("assets/tries.json", "r") as o:
            tries_list = json.loads(o.read())
    else:
        tries_list = {}
        json_object = json.dumps(tries_list, indent=4)
        with open("assets/tries.json", "w") as o:
            o.write(json_object)

    global scores_list
    if os.path.exists("assets/scores.json"):
        with open("assets/scores.json", "r") as o:
            scores_list = json.loads(o.read())
    else:
        scores_list = {}
        json_object = json.dumps(scores_list, indent=4)
        with open("assets/scores.json", "w") as o:
            o.write(json_object)


    global names_list
    names_list = {}
    global names_loaded 
    names_loaded = False
    asyncio.ensure_future(get_names())
