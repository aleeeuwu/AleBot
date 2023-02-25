from discord.ext import commands
import random
import requests as req

@commands.hybrid_command(description='Sends a random Garfield strip from GoComics. Command functionality made by kittrz.')
async def garfield(ctx):
    r = req.get("https://www.gocomics.com/random/garfield").text
    urlIndex = r.find("src=\"https://assets.amuniversal");
    str = ""
    # weird jank because I can't get the string array thing to print out right
    for i in range(5, 68):
        str += r[urlIndex+i]
    #ale added this. dumb way to check if the site works but i wanted to do it
    if 'https://assets.amuniversal.com/' not in str:
        await ctx.send('Seems like the site is currently down. Please try again later.')
        return
    await ctx.send(str)

@commands.hybrid_command(description='Sends a random Heathcliff strip from GoComics. Command functionality made by kittrz.')
async def heathcliff(ctx):
    r = req.get("https://www.gocomics.com/random/heathcliff").text
    urlIndex = r.find("src=\"https://assets.amuniversal");
    str = ""
    # weird jank because I can't get the string array thing to print out right
    for i in range(5, 68):
        str += r[urlIndex+i]
    #ale added this. dumb way to check if the site works but i wanted to do it
    if 'https://assets.amuniversal.com/' not in str:
        await ctx.send('Seems like the site is currently down. Please try again later.')
        return
    await ctx.send(str)

@commands.hybrid_command(description='Sends a random Garfield Minus Garfield strip. Command functionality made by kittrz.')
async def jon(ctx):
    r = req.get("https://garfieldminusgarfield.net/page/0").text 
    
    firstComicIndex = r.find("lastpage")
    
    # this is jank and I don't know if this will even work when the site is updated
    for i in range(0, 20):
        if r[firstComicIndex-i] == '/':
            for j in range(0, 10):
                r[firstComicIndex-i+j] 
                if r[firstComicIndex-i+j] == '\"':
                     firstComicIndex = r[firstComicIndex-i+1:firstComicIndex-i+j]
                     break
            break
    
    r = req.get("https://garfieldminusgarfield.net/page/" + str(random.randrange(0,int(firstComicIndex)))).text
#urlIndex = r.find("src=\"https://assets.amuniversal");
    urlIndex = r.find("<img src=\"https://64.media.tumblr.")
    urlIndex2 = r.rfind("<img src=\"https://64.media.tumblr.")
    link1 = ""
    link2 = ""
# weird jank because I can't get the string array thing to print out right
    for i in range(10, 200):
        if r[urlIndex+i] == '\"':
            break
        link1 += r[urlIndex+i]
# repeated code, could probably be made better
    for i in range(10, 200):
        if r[urlIndex2+i] == '\"':
            break
        link2 += r[urlIndex2+i]
    outputLink = ""
    if(random.randint(0, 1) == 0):
        outputLink = link1
    else:
        outputLink = link2
    #ale added this. dumb way to check if the site works but i wanted to do it
    if 'https://64.media.tumblr.' not in outputLink:
        await ctx.send('Seems like the site is currently down. Please try again later')
        return
    await ctx.send(outputLink)

async def setup(bot):
    bot.add_command(garfield)
    bot.add_command(heathcliff)
    bot.add_command(jon)
