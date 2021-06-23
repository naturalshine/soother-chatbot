#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module creates intent parsers for the adapt engine.
"""
from adapt.intent import IntentBuilder


# General purpose keywords
switch_keywords = [
    'change',
    'switch'
]

play_keywords = [
    'play',
    'role play',
    'act like',
    'pretend'
]

different_keywords = [
    'new',
    'different',
    'another',
    'other'
]

dog_keywords = [
    'dog',
    'shrink',
    'psychiatrist',
    'doctor'
]

alien_keywords = [
    'alien',
    'jellyfish',
    'claire'
]

friend_keywords = [
    'friend',
    'trapped',
    'time'
]

exit_keywords = [
    'leave',
    'bye',
    'exit',
    'quit',
    'goodbye',
    'later',
    'farewell'
]


menu_keywords = [
    'menu',
    'what else can you do',
    'something else',
    'what are my options',
    'what else',
    'help',
    'what can you do'
]
#appointment_regex_keywords = ['{} (?P<Appointment>(?:(?!with|at).)*)'.format(keyword)
#for keyword in appointment_keywords]
with_regex_keyword = 'with (?P<With>\S*)'
#location_regex_keyword = 'at (?P<Location>\S*)'


# General purpose regex keywords
#entry_regex_keywords = ['{} (?P<Entry>[0-9]*)'.format(keyword)
                        #for keyword_group in [todo_keywords, appointment_keywords]
                        #for keyword in keyword_group]


# context should be added as requirement here
quit_intent = IntentBuilder('QuitIntent')\
    .require('ExitKeyword')\
    .optionally('PleaseKeyword')\
    .build()

menu_intent = IntentBuilder('MenuIntent')\
    .require('MenuKeyword')\
    .optionally('PleaseKeyword')\
    .build()

change_intent = IntentBuilder('ChangeRoleIntent')\
    .require('SwitchKeyword')\
    .optionally('DifferentKeyword')\
    .build()

play_intent = IntentBuilder('RolePlayIntent')\
    .require('PlayKeyword')\
    .build()

dog_intent = IntentBuilder('PlayDogIntent')\
    .require('DogKeyword')\
    .optionally('PlayKeyword')\
    .build()

alien_intent = IntentBuilder('PlayAlienIntent')\
    .require('AlienKeyword')\
    .optionally('PlayKeyword')\
    .build()

friend_intent = IntentBuilder('PlayFriendIntent')\
    .require('FriendKeyword')\
    .optionally('PlayKeyword')\
    .build()

# Regular entity groups
entities = {
    'ExitKeyword': exit_keywords,
    'MenuKeyword': menu_keywords, 
    'PlayKeyword': play_keywords,
    'SwitchKeyword': switch_keywords,
    'DifferentKeyword': different_keywords,
    'DogKeyword': dog_keywords,
    'AlienKeyword': alien_keywords,
    'FriendKeyword': friend_keywords
}
# List of lists of regular expression entities
#multi_regex_entities = [todo_regex_keywords, appointment_regex_keywords,
                        #entry_regex_keywords]
# List of regular expression entity strings
single_regex_entities = [with_regex_keyword]

skill_intents = [change_intent, play_intent, dog_intent, alien_intent, friend_intent, quit_intent, menu_intent]

