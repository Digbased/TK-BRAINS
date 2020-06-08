import discord
from discord.ext import commands
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from collections import defaultdict

POET_LINKS = list()
WARRIOR_LINKS = list()
ALL_LINKS = list()
MAGE_LINKS = list()
ROGUE_LINKS = list()

ALL_DICT = defaultdict(lambda: tuple())
POET_DICT = defaultdict(lambda: tuple())
WARRIOR_DICT = defaultdict(lambda: tuple())
MAGE_DICT = defaultdict(lambda: tuple())
ROGUE_DICT = defaultdict(lambda: tuple())

def getPoetData() -> None:

    global POET_LINKS
    
    url = 'http://users.nexustk.com/webreport/PowerPoet.htm'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    temp = soup.findAll('a')

    POET_LINKS = [line.attrs['href'] for line in temp]

def getMageData() -> None:

    global MAGE_LINKS
    
    url = 'http://users.nexustk.com/webreport/PowerMage.htm'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    temp = soup.findAll('a')

    MAGE_LINKS = [line.attrs['href'] for line in temp]

def getRogueData() -> None:

    global ROGUE_LINKS
    
    url = 'http://users.nexustk.com/webreport/PowerRogue.htm'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    temp = soup.findAll('a')

    ROGUE_LINKS = [line.attrs['href'] for line in temp]

def getAllData() -> None:

    global ALL_LINKS
    
    url = 'http://users.nexustk.com/webreport/PowerAll.htm'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    temp = soup.findAll('a')

    ALL_LINKS = [line.attrs['href'] for line in temp]

def getWarriorData() -> None:

    global WARRIOR_LINKS
    
    url = 'http://users.nexustk.com/webreport/PowerWarrior.htm'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    temp = soup.findAll('a')

    WARRIOR_LINKS = [line.attrs['href'] for line in temp]

def storePoetNames() -> None:

    global POET_DICT
    global POET_LINKS
    count = 1
    
    for line in POET_LINKS:
        line = line.strip().split('=')
        POET_DICT[line[1].lower()] = (line[0] + '=' + line[1], count)

        count += 1

def storeMageNames() -> None:

    global MAGE_LINKS
    global MAGE_DICT
    count = 1
    
    for line in MAGE_LINKS:
        line = line.strip().split('=')
        MAGE_DICT[line[1].lower()] = (line[0] + '=' + line[1], count)

        count += 1

def storeRogueNames() -> None:

    global ROGUE_LINKS
    global ROGUE_DICT
    count = 1
    
    for line in ROGUE_LINKS:
        line = line.strip().split('=')
        ROGUE_DICT[line[1].lower()] = (line[0] + '=' + line[1], count)

        count += 1

def storeWarriorNames() -> None:

    global WARRIOR_DICT
    global WARRIOR_LINKS
    count = 1
    
    for line in WARRIOR_LINKS:
        line = line.strip().split('=')
        WARRIOR_DICT[line[1].lower()] = (line[0] + '=' + line[1], count)

        count += 1

def storeAllNames() -> None:

    global ALL_DICT
    global ALL_LINKS
    count = 1
    
    for line in ALL_LINKS:
        line = line.strip().split('=')
        ALL_DICT[line[1].lower()] = (line[0] + '=' + line[1], count)

        count += 1
