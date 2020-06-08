import discord
from discord.ext import commands
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from collections import defaultdict
import math



def CalcEXP(cv, cm, dv, dm):

    vitaDiff = dv - cv
    manaDiff = dm - cm


    return vitaDiff, manaDiff
    

def EXP(vita, mana):
    
    Experience = float()
    VSells = math.floor(vita / 100)
    MSells = math.floor(mana / 50)
    VSegments=math.floor((VSells-1000)/(200))
    MSegments=math.floor((MSells-1000)/(200))
    
    if (vita<100000):
        VCost=20
        Experience=VSells*20
    else:
        VCost=math.floor(((((math.floor(vita/20000))*4)-((math.floor(vita/20000)-6)*2))))
        Experience=(VSells*20) + (((((2*VSegments)+20+22)/2)-20) * (VSegments*200)) +((VSells-1000-(VSegments*200))*(VCost-20))

    if (mana<50000):
        MCost=20
        Experience+=MSells*20
    else:
        MCost=math.floor(((((math.floor(mana/10000))*4)-((math.floor(mana/10000)-6)*2))))
        Experience+=(MSells*20) + (((((2*MSegments)+20+22)/2)-20) * (MSegments*200)) +((MSells-1000-(MSegments*200))*(MCost-20))

    return Experience * 1000000

