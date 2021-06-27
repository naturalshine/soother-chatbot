#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module creates intent parsers for the adapt engine.
"""
from adapt.intent import IntentBuilder


asmr_keywords = [
    'tingles',
    'asmr',
    'autonomous sensory meridian response',
    'braingasm'
]


triggers_keywords = [
    'trigger',
    'whispering',
    'nail',
    'hair',
    'scissors',
    'drawing',
    'visual',
    'bubble wrap',
    'crinkling',
    'marker',
    'tea',
    'water',
    'shower',
    'crinkle',
    'whisper',
    'nail tapping',
    'tapping',
    'ear',
    'scalp',
    'head',
    'mouth',
    'spit',
    'saliva',
    'skin',
    'fabric',
    'clothes',
    'bottle',
    'bottles',
    'bubbles',
    'bubble'

]

therapy_keywords = [
    'insomnia',
    'anxiety',
    'loneliness',
    'therapy',
    'therapeutic',
    'psychological',
    'nursing',
    'care',
    'soothing',
    'calming',
    'calm',
    'meditative',
    'caring',
    'why'
]

about_keywords = [
    'about',
    'tell me',
    'what is',
    'what\'s',
    'the deal',
    'more about'
]

please_keywords = [
    'please',
    'bitte'
]

thanks_keywords = [
    'thanks',
    'thank you'
]

no_keywords = [
    'no',
    'nope',
    'nein',
    'naw',
    'that\'s it',
    'that\'s all',
    'nothing',
    'none'
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


menu_keywords = [
    'menu',
    'what else can you do',
    'something else',
    'what are my options',
    'what else',
    'what can you do',
    'help'
]

history_keywords = [
    'where does it come from',
    'history',
    'started',
    'come from',
    'how long',
    'who'
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

about_asmr_intent = IntentBuilder("AboutAsmrIntent")\
    .require('AboutKeyword')\
    .require('AsmrKeyword')\
    .build()



menu_intent = IntentBuilder('MenuIntent')\
    .require('MenuKeyword')\
    .optionally('PleaseKeyword')\
    .build()

trigger_intent = IntentBuilder('TriggerIntent')\
    .require('AsmrContext')\
    .require('TriggerKeyword')\
    .optionally('AsmrKeyword')\
    .build()

therapeutic_intent = IntentBuilder('TherapeuticIntent')\
    .require('AsmrContext')\
    .require('TherapyKeyword')\
    .optionally('AsmrKeyword')\
    .build()

history_intent = IntentBuilder('HistoryIntent')\
    .require('AsmrContext')\
    .require('HistoryKeyword')\
    .optionally('AsmrKeyword')\
    .build()

# Regular entity groups
entities = {
    'ExitKeyword': exit_keywords,
    'MenuKeyword': menu_keywords, 
    'AsmrKeyword': asmr_keywords,
    'AboutKeyword': about_keywords,
    'TherapyKeyword': therapy_keywords,
    'TriggerKeyword': triggers_keywords,
    'HistoryKeyword': history_keywords,
}

# List of lists of regular expression entities
#multi_regex_entities = [todo_regex_keywords, appointment_regex_keywords,
                        #entry_regex_keywords]
# List of regular expression entity strings
single_regex_entities = [with_regex_keyword]

skill_intents = [menu_intent, history_intent, therapeutic_intent, trigger_intent, about_asmr_intent, quit_intent]

