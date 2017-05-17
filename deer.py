#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
DeerBot V 0.10 - KaTT/DetKraken
Basic bot to neh at people and beg for food occationally

Version 0.15~ - Added neh functionality & broke neh
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

    # If the rng is greater than 5 and the neh cooldown is less or equal 0 then neh!
    def neh(self):
        rgn = randomint(0,10)
        print(rgn)
        if rgn < 5 and self.neh_cooldown <= 0:

            # vvvvFix this!!vvvv
            channel.send_message('Neh!')
            # ^^^^Fix this!!^^^^

            self.times_nehd += 1
            self.neh_cooldown = self.cooldown_time
        else:
            print('neh_cooldown before = {}').format(self.neh_cooldown)
            self.neh_cooldown -= randomint(0,3)
            print('after {}').format(self.neh_cooldown)

    # If pet replies with a message, make a list and change em up
    def pet(self, event):
        event.msg.reply('*accepts ur grooms*')
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

# Deer created :^)
deer = Deer()

# Initialized Discord server info
server = Guild()