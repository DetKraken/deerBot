#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
DeerBot V 0.20 - KaTT/DetKraken
Basic bot to neh at people and beg for food occationally

Version 0.20 - Pet "fully" implemented, create a way to add to it via deer commands?
               Neh still broken

Version 0.15 - Added neh functionality & broke neh
Version 0.10 - First commit
'''

from disco import client
from disco.bot import Bot, Plugin
from disco.types import Channel, Guild
import time, datetime, random


# The actual deer class, contains deer actions and variables
class Deer():
    def __init__(self):

        # Initializing variables
        self.active = True
        self.woke_up = datetime.datetime.now()
        self.cooldown_time = 60
        self.times_nehd = 0
        self.times_pet = 0
        self.times_fed = 0
        self.times_begged = 0
        self.neh_cooldown = 1

    # If the rng is greater than 7 and the neh cooldown is less or equal 0 then neh!
    def neh(self):
        rgn = randomint(0,10)
        if rgn < 7 and self.neh_cooldown <= 0:

            # vvvvFix this!!vvvv
            print('neh')
            # ^^^^Fix this!!^^^^

            self.times_nehd += 1
            self.neh_cooldown = self.cooldown_time

        # Else, subtract from cooldown by a randomized amount
        else:
            self.neh_cooldown -= randomint(0,3)

    # If pet replies with a random message
    def pet(self, event):
        event.msg.reply(randomwordget('pet',randomint(0,3)))
        self.times_pet += 1

    # If food is detected, beg
    def foods(self, event):
        event.msg.reply(':deer::pray:')
        self.times_begged += 1

    # Same deal as pet
    def feed(self, event):
        event.msg.reply('*accepts ur foods*')
        self.times_fed += 1

    # For debug purposes mostly, echoes deer variables
    def stats(self, event):
        stats = ('{} times nehd | {} times pet | {} times fed | {} times begged | Time initialized {}').format(self.times_nehd, self.times_pet, self.times_fed, self.times_begged, self.woke_up)
        event.msg.reply(stats)


class DeerPlugin(Plugin):
    # Deer commands goes here, format '@DeerBot {}'
    @Plugin.command('pet')
    def on_deer_pet(self, event):
        deer.pet(event)

    @Plugin.command('feed')
    def on_deer_fed(self, event):
        deer.feed(event)

    @Plugin.command('stats')
    def on_deer_stats(self, event):
        deer.stats(event)

    @Plugin.command('sleep')
    def on_deer_sleep(self, event):
        deer.active = False
        event.msg.reply('*dozes off~*')

# Initializes a seed and returns a randomly generated int
def randomint(min, max):
    random.seed()
    return random.randint(min, max)

# Reads local .txt files, stores them in a list and returns a random one
def randomwordget(type, rgn):
    dir = 'wordlist/{}.txt'.format(type)
    words = open(dir)
    wordlist = words.readline().split(',')
    return wordlist[rgn]

# Deer created :^)
deer = Deer()

# Initialized Discord server info
server = Guild()