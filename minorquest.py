import discord
from discord.ext import commands
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from collections import defaultdict

MQ_DICT = defaultdict(lambda: list())

def parseMQText(txt):

    global MQ_DICT
    
    with open(txt, 'r') as f:
        try:
            for line in f:
                line = line.strip().split(':')
                MQ_DICT[line[0].lower()].append((line[1], line[2] + line[3]))
        except Exception:
            pass
