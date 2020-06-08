import discord
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from collections import defaultdict
from crawling import *
from minorquest import *
from exp import *
from babel.numbers import format_number, format_decimal, format_percent, parse_decimal

TOKEN = 'NzE3OTg1MTY1MDQwODEyMDUy.Xtr6lg.MLzawLU34F06Ag9etzCI5CJPeeU'

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.command(name='leader')
async def outputAllLeaderboard(ctx, start, end):

    result = "```"
    global ALL_DICT

    try:
        for key, value in ALL_DICT.items():

            if (int(value[1]) >= int(start)):
                if (int(value[1]) <= int(end)):
                    result += str(value[1]) + '. ' + key + '\n'
                    #print(value[1], key)
                    #await ctx.send(str(value[1]) + '. ' + key)
    except Exception as e:
        await ctx.send('```Error Invalid Command or the following: ' + '```')

    result += "```"
    await ctx.send(result)

@bot.command(name='poet-leader')
async def outputPoetLeaderboard(ctx, start, end):

    result = "```"
    global POET_DICT

    try:
        for key, value in POET_DICT.items():

            if (int(value[1]) >= int(start)):
                if (int(value[1]) <= int(end)):
                    result += str(value[1]) + '. ' + key + '\n'
                    #print(value[1], key)
                    #await ctx.send(str(value[1]) + '. ' + key)
    except Exception as e:
        #await ctx.send('```Error Invalid Command or the following: ' + '```')'
        pass

    result += "```"
    await ctx.send(result)

@bot.command(name='warrior-leader')
async def outputWarriorLeaderboard(ctx, start, end):

    result = "```"
    global WARRIOR_DICT

    try:
        for key, value in WARRIOR_DICT.items():

            if (int(value[1]) >= int(start)):
                if (int(value[1]) <= int(end)):
                    result += str(value[1]) + '. ' + key + '\n'
                    #print(value[1], key)
                    #await ctx.send(str(value[1]) + '. ' + key)
    except Exception as e:
        #await ctx.send('```Error Invalid Command or the following: ' + '```')
        pass
    result += "```"
    await ctx.send(result)

@bot.command(name='mage-leader')
async def outputMageLeaderboard(ctx, start, end):

    result = "```"
    global MAGE_DICT

    try:
        for key, value in MAGE_DICT.items():

            if (int(value[1]) >= int(start)):
                if (int(value[1]) <= int(end)):
                    result += str(value[1]) + '. ' + key + '\n'
                    #print(value[1], key)
                    #await ctx.send(str(value[1]) + '. ' + key)
    except Exception as e:
        #await ctx.send('```Error Invalid Command or the following: ' + '```')
        pass
    result += "```"
    await ctx.send(result)

@bot.command(name='rogue-leader')
async def outputRogueLeaderboard(ctx, start, end):

    result = "```"
    global ROGUE_DICT

    try:
        for key, value in ROGUE_DICT.items():

            if (int(value[1]) >= int(start)):
                if (int(value[1]) <= int(end)):
                    result += str(value[1]) + '. ' + key + '\n'
                    #print(value[1], key)
                    #await ctx.send(str(value[1]) + '. ' + key)
    except Exception as e:
        #await ctx.send('```Error Invalid Command or the following: ' + '```')
        pass
    result += "```"
    await ctx.send(result)

@bot.command(name='huntexp')
async def displayEXP(ctx, cv, cm, dv, dm):

    cv = int(cv)
    cm = int(cm)
    dv = int(dv)
    dm = int(dm)

    current = EXP(cv, cm)
    desired = EXP(dv, dm)

    difference = desired - current
    result = '```Current Experience: ' + str(format_decimal(current, locale='en_US')) + '\n'
    result += 'Current Vita: ' + str(cv) + '\n'
    result += 'Current Mana: ' + str(cm) + '\n'
    result += 'Desired Vita: ' + str(dv) + '\n'
    result += 'Desired Mana: ' + str(dm) + '\n'
    result += 'Experience Needed: ' + str(format_decimal(difference, locale='en_US')) + '\n'
    result += 'Remaining to Hunt: ' +  str(format_decimal(difference/4294000000, locale='en_US')) + ' maxes```'
    
    await ctx.send(result)

# !server
@bot.command(name='server')
async def serverStatus(ctx):
    
    url = 'http://users.nexustk.com/ServerStatus/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "xml")

    temp = soup.get_text()
    x = temp.strip().split('\n')

    result = '```'


    for index, data in enumerate(x):
        if data.startswith(' RunningLogin server'):
            result += 'Total Users Online: ' + str(data[20:]) + ' users\n'
            #await ctx.send('Login: ' + str(data[20:]) + ' users')
        elif data.startswith(' RunningNation server'):
            result += 'Nation: ' + str(data[21:]) + ' users\n'
            #await ctx.send('Nation: ' + str(data[21:]) + ' users')
        elif data.startswith(' RunningCarnage server'):
            result += 'Carnage: ' + str(data[22:]) + ' users\n'
            #await ctx.send('Carnage: ' + str(data[22:]) + ' users')
        elif data.startswith(' RunningEvent server'):
            result += 'Event: ' + str(data[20:]) + ' users\n'
            #await ctx.send('Event: ' + str(data[20:]) + ' users')

    result += '```'

    await ctx.send(result)

# !pk
@bot.command(name='pk')
async def parsePK(ctx):
    # url needs to be updated until I can parse in real-time.
    # Probably selenium
    LINKS = list()
    url = 'http://boards.nexustk.com/carnage/Drywater%2005310033.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "xml")
    temp = soup.get_text()[:1992].strip()
    final = soup.get_text()[1993:].strip()
    await ctx.send("```" + temp + "```")
    await ctx.send("```" + final + "```")
    
# !poet    
@bot.command(name='poet')
async def getPoetUserData(ctx, arg1):
    global POET_DICT

    result = str()
    temp = arg1.lower()

    try:
        url = POET_DICT[arg1][0]
        rank = POET_DICT[arg1][1]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script","style"]):
            script.extract()

        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        #print(type(text))
        data = text.split('\n')
        #print(data)

        #print('\n')
        temp = 'https://melfy.me/tk/user/'
        result = "```Name: " + arg1 + "\n"
        result += "Profile powered by Melfy: " + temp + arg1 + "\n"
        
        #await ctx.send('Name: ' + arg1)
        for item in data:
            if item.startswith('Vita :'):
                result += 'Vita: ' + str( item[6:]) + '\n'
                #await ctx.send('Vita: ' + str( item[6:]))
            elif item.startswith('Mana :'):
                result += 'Mana: ' + str(item[6:]) + '\n'
                #await ctx.send('Mana: ' + str(item[6:]))
            elif item.startswith('Level :'):
                result += 'Level: ' + str(item[7:]) + '\n'
                #await ctx.send('Level: ' + str(item[7:]))
            elif item.startswith('Clan title:'):
                result += 'Clan title: ' + str( item[11:]) + '\n'
                #await ctx.send('Clan title: ' + str( item[11:]))
            elif item.startswith('Blood brother :'):
                result += 'Blood brother: ' + str(item[15:]) + '\n'
                #await ctx.send('Blood brother: ' + str(item[15:]))
            elif item.startswith('Has won '):
                result += 'KSG wins: ' + str(item[8]) + '\n'
                #await ctx.send('KSG wins: ' + str(item[8]))
                

        result += 'Path Leaderboard rank: ' + str( rank) + '```'
        #await ctx.send('Path Leaderboard rank: ' + str( rank))
        #print(url)

    except Exception as e:
        #await ctx.send('Character not Found. Error listed: ' + e)
        print(e)

    await ctx.send(result)

@bot.command(name='warrior')
async def getWarriorUserData(ctx, arg1):
    global WARRIOR_DICT

    result = str()
    temp = arg1.lower()

    try:
        url = WARRIOR_DICT[arg1][0]
        rank = WARRIOR_DICT[arg1][1]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script","style"]):
            script.extract()

        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        #print(type(text))
        data = text.split('\n')
        #print(data)

        #print('\n')

        result = "```Name: " + arg1 + "\n"
        
        #await ctx.send('Name: ' + arg1)
        for item in data:
            if item.startswith('Vita :'):
                result += 'Vita: ' + str( item[6:]) + '\n'
                #await ctx.send('Vita: ' + str( item[6:]))
            elif item.startswith('Mana :'):
                result += 'Mana: ' + str(item[6:]) + '\n'
                #await ctx.send('Mana: ' + str(item[6:]))
            elif item.startswith('Level :'):
                result += 'Level: ' + str(item[7:]) + '\n'
                #await ctx.send('Level: ' + str(item[7:]))
            elif item.startswith('Clan title:'):
                result += 'Clan title: ' + str( item[11:]) + '\n'
                #await ctx.send('Clan title: ' + str( item[11:]))
            elif item.startswith('Blood brother :'):
                result += 'Blood brother: ' + str(item[15:]) + '\n'
                #await ctx.send('Blood brother: ' + str(item[15:]))
            elif item.startswith('Has won '):
                result += 'KSG wins: ' + str(item[8]) + '\n'
                #await ctx.send('KSG wins: ' + str(item[8]))
                

        result += 'Path Leaderboard rank: ' + str( rank) + '```'
        #await ctx.send('Path Leaderboard rank: ' + str( rank))
        #print(url)

    except Exception as e:
        #await ctx.send('Character not Found. Error listed: ' + e)
        print(e)

    await ctx.send(result)

@bot.command(name='mage')
async def getMageUserData(ctx, arg1):

    global MAGE_DICT

    result = str()
    temp = arg1.lower()

    try:
        url = MAGE_DICT[arg1][0]
        rank = MAGE_DICT[arg1][1]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script","style"]):
            script.extract()

        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        #print(type(text))
        data = text.split('\n')
        #print(data)

        #print('\n')

        result = "```Name: " + arg1 + "\n"
        
        #await ctx.send('Name: ' + arg1)
        for item in data:
            if item.startswith('Vita :'):
                result += 'Vita: ' + str( item[6:]) + '\n'
                #await ctx.send('Vita: ' + str( item[6:]))
            elif item.startswith('Mana :'):
                result += 'Mana: ' + str(item[6:]) + '\n'
                #await ctx.send('Mana: ' + str(item[6:]))
            elif item.startswith('Level :'):
                result += 'Level: ' + str(item[7:]) + '\n'
                #await ctx.send('Level: ' + str(item[7:]))
            elif item.startswith('Clan title:'):
                result += 'Clan title: ' + str( item[11:]) + '\n'
                #await ctx.send('Clan title: ' + str( item[11:]))
            elif item.startswith('Blood brother :'):
                result += 'Blood brother: ' + str(item[15:]) + '\n'
                #await ctx.send('Blood brother: ' + str(item[15:]))
            elif item.startswith('Has won '):
                result += 'KSG wins: ' + str(item[8]) + '\n'
                #await ctx.send('KSG wins: ' + str(item[8]))
                

        result += 'Path Leaderboard rank: ' + str( rank) + '```'
        #await ctx.send('Path Leaderboard rank: ' + str( rank))
        #print(url)

    except Exception as e:
        #await ctx.send('Character not Found. Error listed: ' + e)
        print(e)

    await ctx.send(result)

@bot.command(name='rogue')
async def getRogueUserData(ctx, arg1):
    global ROGUE_DICT

    result = str()
    temp = arg1.lower()

    try:
        url = ROGUE_DICT[arg1][0]
        rank = ROGUE_DICT[arg1][1]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script","style"]):
            script.extract()

        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        #print(type(text))
        data = text.split('\n')
        #print(data)

        #print('\n')

        result = "```Name: " + arg1 + "\n"
        
        #await ctx.send('Name: ' + arg1)
        for item in data:
            if item.startswith('Vita :'):
                result += 'Vita: ' + str( item[6:]) + '\n'
                #await ctx.send('Vita: ' + str( item[6:]))
            elif item.startswith('Mana :'):
                result += 'Mana: ' + str(item[6:]) + '\n'
                #await ctx.send('Mana: ' + str(item[6:]))
            elif item.startswith('Level :'):
                result += 'Level: ' + str(item[7:]) + '\n'
                #await ctx.send('Level: ' + str(item[7:]))
            elif item.startswith('Clan title:'):
                result += 'Clan title: ' + str( item[11:]) + '\n'
                #await ctx.send('Clan title: ' + str( item[11:]))
            elif item.startswith('Blood brother :'):
                result += 'Blood brother: ' + str(item[15:]) + '\n'
                #await ctx.send('Blood brother: ' + str(item[15:]))
            elif item.startswith('Has won '):
                result += 'KSG wins: ' + str(item[8]) + '\n'
                #await ctx.send('KSG wins: ' + str(item[8]))
                

        result += 'Path Leaderboard rank: ' + str( rank) + '```'
        #await ctx.send('Path Leaderboard rank: ' + str( rank))
        #print(url)

    except Exception as e:
        #await ctx.send('Character not Found. Error listed: ' + e)
        print(e)

    await ctx.send(result)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@bot.event
async def on_ready():

    await bot.change_presence(activity=discord.Game(name="Powered by zerent"))

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='minorquest')
async def getMQ(ctx, arg1, arg2):

    global MQ_DICT

    arg1 =  arg1.lower()
    arg2 = arg2.lower()

    monster = arg1 + ' ' + arg2
    monster.strip()
    
    #result = '```'
    #print(arg1)

    #print(MQ_DICT)

    try:
        for items in MQ_DICT[monster]:
            result = '```'
            result += 'Monster Name: ' + monster + '\n'
            result += 'Location: ' + items[0] + '\n'
            result += 'URL: ' + items[1] + '\n'
            result += '```'
            await ctx.send(result)
    except Exception:
        await ctx.send('```Monster not found, try again```')

    '''
    try:
        for key, value in MQ_DICT.items():
                if key == monster:
                    for item in value:
                        result = '```'
                        result += 'Monster Name: ' + key + '\n'
                        result += 'Location: ' + item[0] + '\n'
                        result += 'URL: ' + item[1] + '\n'
                        result += '```'
                        await ctx.send(result)
    except Exception:
        pass
    '''
    #result += '```'
    #await ctx.send(result)


@bot.command(name='cmds')
async def novice(ctx):
    help_string = """```
    !minorquest <monster>
    !server
    !rogue <char name>
    !mage <char name>
    !poet <char name>
    !warrior <char name>
    !poet-leader <start rank> <end rank>
    !warrior-leader <start rank> <end rank>
    !leader <start rank> <end rank>
    !huntexp <> <> <> <>
    
    ```
    """

    await ctx.send(help_string)

def main():
    
    getPoetData( )
    storePoetNames( )
    getWarriorData()
    storeWarriorNames()
    getAllData()
    storeAllNames()
    getRogueData()
    storeRogueNames()
    getMageData()
    storeMageNames()
    parseMQText('minorquest.txt')


    bot.run(TOKEN)

main()
