#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module creates intent parsers for the adapt engine.
"""
from adapt.intent import IntentBuilder


start_keywords = [
    'dog',
    'therapist',
    'play dog',
    'role play',
    'role play dog',
    'be my therapist',
    'be my dog',
    'start role play',
    'start'
]

feeling_keywords = [
    'sad',
    'lonely',
    'alone',
    'bored',
    'happy',
    'anxious',
    'joyful',
    'angry',
    'annoyed',
    'upset',
    'afraid'
]

therapy_keywords = [
    'life',
    'what am I doing',
    'what should I do',
    'existential crisis',
    'isolation',
    'I don\'t know',
    'don\'t know',
    'what could I do'
]

existential_keywords = [
    'what is a good life',
    'what is life',
    'why are we here',
    'what is to be done',
    'how should i live?',
    'live',
    'life',
    'alive',
    'good person',
    'good human',
    'why',
    'who am I',
    'who is anyone',
    'what is'
]

help_keywords = [
    'help',
    'help me'
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
    'what can you do'
]

history_keywords = [
    'where does it come from',
    'history',
    'started',
    'come from',
    'how long'
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

about_dog_intent = IntentBuilder("AboutDog")\
    .require('AboutKeyword')\
    .build()

existential_intent = IntentBuilder("ExistentialIntent")\
    .require('ExistentialKeyword')\
    .build()

history_intent = IntentBuilder('HistoryIntent')\
    .require('HistoryKeyword')\
    .build()

feeling_intent = IntentBuilder('FeelingIntent')\
    .require("FeelingKeyword")\
    .build()

therapy_intent = IntentBuilder('TherapyIntent')\
    .require("TherapyKeyword")\
    .build()

yes_intent = IntentBuilder('YesIntent')\
    .require('YesKeyword')\
    .build()

no_intent = IntentBuilder('NoIntent')\
    .require('NoKeyword')\
    .build()

soother_intent = IntentBuilder('SootherKeyword')\
    .require('SootherKeyword')\
    .build()

start_intent = IntentBuilder('StartIntent')\
    .require('StartKeyword')\
    .build()

# Regular entity groups
entities = {
    'ExitKeyword': exit_keywords,
    'MenuKeyword': menu_keywords, 
    'TherapyKeyword': therapy_keywords,
    'FeelingKeyword': feeling_keywords,
    'HistoryKeyword': history_keywords,
    'ExistentialKeyword': existential_keywords,
    'AboutKeyword': about_keywords,
    'YesKeyword': yes_keywords,
    'NoKeyword': no_keywords,
    'SootherKeyword': soother_keywords,
    'StartKeyword': start_keywords
}

# List of lists of regular expression entities
#multi_regex_entities = [todo_regex_keywords, appointment_regex_keywords,
                        #entry_regex_keywords]
# List of regular expression entity strings
single_regex_entities = [with_regex_keyword]

skill_intents = [menu_intent, quit_intent, therapy_intent, feeling_intent, history_intent, existential_intent, about_dog_intent, yes_intent, no_intent, soother_intent, start_intent]

