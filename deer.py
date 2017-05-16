#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
DeerBot V 0.10 - KaTT/DetKraken
Basic bot to neh at people and beg for food occationally

Version 0.10 - Master
'''

from disco.bot import Bot, Plugin
import datetime

# The actual deer class, contains deer actions and variables
class deer():
    def __init__(self):

        #Initializes variables
        self.woke_up = datetime.datetime.now()
        self.times_nehd = 0
        self.times_pet = 0
        self.times_fed = 0
        self.times_begged = 0

    def neh(self, event):
        event.msg.reply('Neh')
        self.times_nehd += 1

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
        stats = ('{} times nehd | {} times pet | {} times fed | {} times begged').format(self.times_nehd, self.times_pet, self.times_fed, self.times_begged)
        event.msg.reply(stats)

# Deer created :^)
deer = deer()

class DeerPlugin(Plugin):
     # Deer commands goes here, format 'deer {}'
    @Plugin.command('deer', '<content:str...>')
    def on_deer_command(self, event, content):
        if content == 'pet':
            deer.pet(event)
        if content == 'feed':
            deer.feed(event)
        if content == 'stats':
            deer.stats(event)