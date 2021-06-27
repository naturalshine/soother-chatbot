#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module creates intent parsers for the adapt engine.
"""
from adapt.intent import IntentBuilder


soother_keywords = [
    'soother',
    'you',
    'it'
]

who_keywords = [
    'who is',
    'what is',
    'who\'s',
    'who',
]

claire_keywords = [
    'claire',
    'tolan',
    'c s t'
]

project_keywords = [
    'project',
    'funded',
    'fund',
]

origin_keywords = [
    'come from',
    'originate',
    'make',
    'made',
    'create',
    'created',
    'where',
    'build',
    'developed',
    'develop',
    'build'
]

dream_keywords = [
    'dream',
    'sleep'
]

epistem_keywords = [
    'what',
    'what are',
    'what is',
    'who',
    'about',
    'tell me',
    'what is',
    'what\'s',
    'the deal',
    'more about'
]

why_keywords = [
    'why',
    'reason',
    'justification',
    'intent',
    'intentione'
]

how_keywords = [
    'how',
    'tools'
]



actually_keywords = [
    'really',
    'actually',
    'behind the curtain',
    'under the sheets',
    'behind the screen',
    'inside the jar',
    'inside the hollow',
    'hollow',
    'inside',
    'persona',
    'behind'
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

what_soother_intent = IntentBuilder('WhatSootherIntent')\
    .require('EpistemKeyowrd')\
    .require('SootherKeyword')\
    .optionally('OriginKeyword')\
    .build()

what_soother_really_intent = IntentBuilder('WhatSootherReallyIntent')\
    .require("ActuallyKeyword")\
    .require("SootherKeyword")\
    .require("EpistemKeyword")\
    .optionally("OriginKeyword")\
    .build()

who_created_intent = IntentBuilder('WhoCreatedIntent')\
    .require('WhoKeyword')\
    .require('OriginKeyword')\
    .build()

who_claire_intent = IntentBuilder('WhoClaireIntent')\
    .require('ClaireKeyword')\
    .optionally('WhoKeyword')\
    .optionally('EpistemKeyword')\
    .optionally('OriginKeyword')\
    .build()

who_funded_intent = IntentBuilder('WhoFundedIntent')\
    .require('WhoKeyword')\
    .require('ProjectKeyword')\
    .build()

why_created_intent = IntentBuilder('WhyCreatedIntent')\
    .require('WhyKeyword')\
    .require('OriginKeyword')\
    .optionally('ProjectKeyword')\
    .optionally('SootherKeyword')\
    .build()

how_created_intent = IntentBuilder('HowCreatedIntent')\
    .require('HowKeyword')\
    .require('OriginKeyword')\
    .build()

soother_dream_intent = IntentBuilder('SootherDreamIntent')\
    .require("DreamKeyword")\
    .require("SootherKeyword")\
    .build()

# Regular entity groups
entities = {
    'ExitKeyword': exit_keywords,
    'MenuKeyword': menu_keywords, 
    'DreamKeyword': dream_keywords,
    'HowKeyword': how_keywords,
    'OriginKeyword': origin_keywords,
    'WhyKeyword': why_keywords,
    'ProjectKeyword': project_keywords,
    'WhoKeyword': who_keywords,
    'EpistemKeyword': epistem_keywords,
    'ClaireKeyword': claire_keywords,
    'ActuallyKeyword': actually_keywords,
    'SootherKeyword': soother_keywords
}

# List of lists of regular expression entities
#multi_regex_entities = [todo_regex_keywords, appointment_regex_keywords,
                        #entry_regex_keywords]
# List of regular expression entity strings
single_regex_entities = [with_regex_keyword]

skill_intents = [menu_intent, quit_intent, soother_dream_intent, how_created_intent, why_created_intent, who_funded_intent, who_claire_intent, who_created_intent, what_soother_intent, what_soother_really_intent]

