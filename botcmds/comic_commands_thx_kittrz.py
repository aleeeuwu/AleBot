from discord.ext import commands
from datetime import datetime, timedelta
import json
import random
import requests as req

@commands.hybrid_command(description='Sends a random Garfield strip from GoComics.')
async def garfield(ctx):
    # start and end dates for the comic, currently assuming strips were released daily
    start = datetime(1978, 6, 19)
    end = datetime.today() # assumes new strips are still releasing

    # calculate number of days between start and end, generate a random number in that range, and use it to find a new date
    delta = end - start
    random_delta = random.randint(0, delta.days)
    random_date = start + timedelta(days=random_delta)

    # fetch the comic
    url = "https://www.gocomics.com/api/service/v2/assets/recent/garfield?date=" + datetime.strftime(random_date, "%Y-%m-%d")
    comic_data_raw = req.get(url).text
    comic_data = json.loads(comic_data_raw)[0]

    await ctx.send(comic_data.get("url"))

@commands.hybrid_command(description='Sends a random Heathcliff strip from GoComics.')
async def heathcliff(ctx):
    # start and end dates for the comic, currently assuming strips were released daily
    start = datetime(2002, 1, 1)
    end = datetime.today() # assumes new strips are still releasing

    # calculate number of days between start and end, generate a random number in that range, and use it to find a new date
    delta = end - start

    # GoComics has some gaps in the daily comics for Heathcliff at the beginning, so this accounts for that
    while True:
        random_delta = random.randint(0, delta.days)

        if not (4 <= random_delta <= 130 or random_delta == 137):
            break

    random_date = start + timedelta(days=random_delta)

    # fetch the comic
    url = "https://www.gocomics.com/api/service/v2/assets/recent/heathcliff?date=" + datetime.strftime(random_date, "%Y-%m-%d")
    comic_data_raw = req.get(url).text
    comic_data = json.loads(comic_data_raw)[0]

    await ctx.send(comic_data.get("url"))

@commands.hybrid_command(description='Sends a random Garfield Minus Garfield strip. Command functionality made by kittrz.')
async def jon(ctx):
    global jon_first_page

    r = req.get("https://garfieldminusgarfield.net/page/" + str(random.randrange(0,int(jon_first_page)))).text
    url_index = r.find("<img src=\"https://64.media.tumblr.")
    url_index_2 = r.rfind("<img src=\"https://64.media.tumblr.")
    link1 = ""
    link2 = ""
# weird jank because I can't get the string array thing to print out right
    for i in range(10, 200):
        if r[url_index+i] == '\"':
            break
        link1 += r[url_index+i]
# repeated code, could probably be made better
    for i in range(10, 200):
        if r[url_index_2+i] == '\"':
            break
        link2 += r[url_index_2+i]
    output_link = ""
    if(random.randint(0, 1) == 0):
        output_link = link1
    else:
        output_link = link2
    #ale added this. dumb way to check if the site works but i wanted to do it
    if 'https://64.media.tumblr.' not in output_link:
        await ctx.send('Seems like the site is currently down. Please try again later')
        return
    await ctx.send(output_link)

async def setup(bot):
    bot.add_command(garfield)
    bot.add_command(heathcliff)

    # get first garfield minus garfield page
    # could break if a new page gets added, but the bot gets reset much more often then any new comics are released so it shouldn't be a big deal
    r = req.get("https://garfieldminusgarfield.net/page/0").text
    
    first_comic_index = r.find("lastpage")

    global jon_first_page
    for i in range(0, 20):
        if r[first_comic_index-i] == '/':
            for j in range(0, 10):
                r[first_comic_index-i+j] 
                if r[first_comic_index-i+j] == '\"':
                     jon_first_page = r[first_comic_index-i+1:first_comic_index-i+j]
                     break
            break

    bot.add_command(jon)
