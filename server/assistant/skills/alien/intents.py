#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module creates intent parsers for the adapt engine.
"""
from adapt.intent import IntentBuilder


start_keywords = [
    'alien',
    'time-travel',
    'play my friend',
    'be my friend',
    'start role play',
    'restart',
    'start',
    'alien roll play',
    'role play',
    'roll play',
    'meditation',
    'meditate'
]

birchwood_keywords = [
    'birch',
    'wood',
    'trees',
    'forest',
    'woods',
    'birchwood',
    'birchwoods'

]

homeplanet_keywords = [
    'planet',
    'center of earth',
    'home planet'
]

smell_keywords = [
    'smell',
    'scent',
    'smells'
]


sound_keywords = [
    'sound',
    'sounds'
]

sensation_keywords = [
    'feels',
    'sensation',
    'feel'

]

norain_keywords = [
    'no',
    'no rain',
    'not raining'

]


rain_keywords = [
    'rain',
    'raining',
    'water',
    'wet'
]

sun_keywords = [
    'sun',
    'light',
    'full sun'
]

shade_keywords = [
    'shade',
    'partial shade',
    'full shade',
    'partial'
]


about_keywords = [
    'about',
    'tell me',
    'what is',
    'what\'s',
    'the deal',
    'more about'
]

no_keywords = [
    'no',
    'nope',
    'nein',
    'naw',
    'that\'s it',
    'that\'s all',
    'nothing',
    'none',
    'whatever',
    'what are you going to do'
]

yes_keywords = [
    'yes',
    'ya',
    'yeah',
    'ja'
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

soother_keywords = [
    'you',
    'you\'re',
    'soother'
]


menu_keywords = [
    'menu',
    'what else can you do',
    'something else',
    'what are my options',
    'what else',
    'what can you do',
    'help'
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

about_alien_intent = IntentBuilder("AboutAlien")\
    .require('AboutKeyword')\
    .build()


start_intent = IntentBuilder('StartIntent')\
    .require('StartKeyword')\
    .build()

birchwood_first_intent = IntentBuilder("BirchwoodFirstIntent")\
    .require('Question1Context')\
    .require('BirchwoodKeyword')\
    .build()

birchwood_shade_intent = IntentBuilder('BirchwoodShadeIntent')\
    .require('ShadeKeyword')\
    .build()

birchwood_sun_intent = IntentBuilder('BirchwoodSunIntent')\
    .require('SunKeyword')\
    .build()

birchwood_sound_intent = IntentBuilder('BirchwoodSoundIntent')\
    .require('BirchwoodSunContext')\
    .require('SoundKeyword')\
    .optionally('YesKeyword')\
    .build()

birchwood_smell_intent = IntentBuilder('BirchwoodSmellIntent')\
    .require('BirchwoodSunContext')\
    .require('SmellKeyword')\
    .optionally('NoKeyword')\
    .build()

birchwood_rain_intent = IntentBuilder('BirchwoodRainIntent')\
    .require('BirchwoodShadeContext')\
    .require('YesKeyword')\
    .optionally('RainKeyword')\
    .build()


birchwood_norain_intent = IntentBuilder('BirchwoodNoRainIntent')\
    .require('BirchwoodShadeContext')\
    .require('NoKeyword')\
    .optionally('NoRainKeyword')\
    .build()


homeplanet_intent = IntentBuilder('HomePlanetIntent')\
    .require('Question1Context')\
    .require('HomePlanetKeyword')\
    .build()

homeplanet_sound_intent = IntentBuilder('HomePlanetSoundIntent')\
    .require('HomePlanetContext')\
    .require('SoundKeyword')\
    .build()

homeplanet_sensation_intent = IntentBuilder('HomePlanetSensationIntent')\
    .require('HomePlanetContext')\
    .require('SensationKeyword')\
    .build()



# Regular entity groups
entities = {
    'ExitKeyword': exit_keywords,
    'MenuKeyword': menu_keywords, 
    'AboutKeyword': about_keywords,
    'StartKeyword': start_keywords,
    'BirchwoodKeyword': birchwood_keywords,
    'NoRainKeyword': norain_keywords,
    'RainKeyword': rain_keywords, 
    'YesKeyword': yes_keywords,
    'NoKeyword': no_keywords, 
    'SmellKeyword': smell_keywords,
    'SoundKeyword': sound_keywords, 
    'SensationKeyword': sensation_keywords,
    'HomePlanetKeyword': homeplanet_keywords,
    'SootherKeyword': soother_keywords,
    'ShadeKeyword': shade_keywords,
    'SunKeyword': sun_keywords
}

# List of lists of regular expression entities
#multi_regex_entities = [todo_regex_keywords, appointment_regex_keywords,
                        #entry_regex_keywords]
# List of regular expression entity strings
single_regex_entities = [with_regex_keyword]

skill_intents = [menu_intent, quit_intent, about_alien_intent, start_intent, birchwood_first_intent, birchwood_norain_intent, birchwood_rain_intent, birchwood_smell_intent, birchwood_sound_intent, birchwood_sun_intent, birchwood_shade_intent, homeplanet_intent, homeplanet_sensation_intent, homeplanet_sound_intent]

