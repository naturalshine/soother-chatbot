#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module creates intent parsers for the adapt engine.
"""
from adapt.intent import IntentBuilder


# General purpose keywords
soother_keywords = [
    'you',
    'this thing',
    'soother',
    'AI',
]

not_soother_keywords = [
    'alexa',
    'siri',
    'google'
]

self_keywords = [
    'me',
    'I',
    'moi'
]

please_keywords = [
    'please',
    'bitte'
]

thanks_keywords = [
    'thanks',
    'thank you'
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

alien_menu_intent = IntentBuilder('AlienMenuIntent')\
    .require('AlienContext')\
    .require('MenuKeyword')\
    .optionally('PleaseKeyword')\
    .build()

dog_menu_intent = IntentBuilder('DogMenuIntent')\
    .require("DogContext")\
    .require("MenuKeyword")\
    .optionally("PleaseKeyword")\
    .build()

friend_menu_intent = IntentBuilder('FriendMenuIntent')\
    .require("FriendContext")\
    .require("MenuKeyword")\
    .optionally("PleaseKeyword")\
    .build()

# Regular entity groups
entities = {
    'ExitKeyword': exit_keywords,
    'MenuKeyword': menu_keywords, 
    'SootherKeyword': soother_keywords,
    'NotSootherKeywords': not_soother_keywords,
    'ThanksKeyword': thanks_keywords,
    'PleaseKeyword': please_keywords,
    'SelfKeyword': self_keywords,
}

# List of lists of regular expression entities
#multi_regex_entities = [todo_regex_keywords, appointment_regex_keywords,
                        #entry_regex_keywords]
# List of regular expression entity strings
single_regex_entities = [with_regex_keyword]

skill_intents = [quit_intent, dog_menu_intent, friend_menu_intent, alien_menu_intent]

