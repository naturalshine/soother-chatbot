#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module creates intent parsers for the adapt engine.
"""
from adapt.intent import IntentBuilder


# General purpose keywords
search_keywords = [
    'search',
    'find',
    'recommend',
    'look for',
    'look up',
    'watch'
]


video_keywords = [
    'video',
    'watch',
    'youtube',
    'vid',
    'vlog',
    'role play'
]

asmr_keywords = [
    'tingles',
    'asmr',
    'autonomous sensory meridian response',
    'braingasm'
]

genre_keywords = [
    'nail tapping',
    'unintentional',
    'hair brushing',
    'ear cleaning',
    'nail polish',
    'whispering',
    'role play',
    'nails',
    'role',
    'polish',
    'hair',
    'ear',
    'brain',
    'visual',
    'trigger',
    'mouth',
    'whisper',
    'sleep',
    'insomnia',
    'anxiety',
    'friend',
    'triggers',
    '360',
    'mouth sounds',
    'saliva',
    'scalp',
    'spine',
    'synesthesia',
    'bottle',
    'bottles',
    'bubbles',
    'mouth',
    'drawing',
    'markers',
    'paint',
    'painting',
    'paint brush',
    'brush',
    'bob ross',
    'canvas',
    'clothes',
    'skin',
    'bubbles',
    'bubble',
    'fizz'
]

roleplay_keywords = [
    'princess',
    'elf',
    'fairy',
    'imp',
    'demon',
    'angel',
    'friend',
    'forest',
    'alien',
    'abduction',
    'exam',
    'doctor',
    'therapist',
    'nurse',
    'devil',
    'seraphim'
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
    'what do you do',
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

about_asmr_intent = IntentBuilder("AboutAsmrIntent")\
    .require('AboutKeyword')\
    .require('AsmrKeyword')\
    .build()


menu_intent = IntentBuilder('MenuIntent')\
    .require('MenuKeyword')\
    .optionally('PleaseKeyword')\
    .build()

search_intent = IntentBuilder('SearchIntent')\
    .optionally('SearchKeyword')\
    .require('AsmrKeyword')\
    .optionally('GenreKeyword')\
    .optionally('PleaseKeyword')\
    .build()

favorite_video_intent = IntentBuilder("FavoriteVideoIntent")\
    .require("FavoriteVideoContext")\
    .require("YesKeyword")\
    .build()

yes_favorite_video_intent = IntentBuilder("YesFavoriteVideoIntent")\
    .require("FavoriteVideoContext")\
    .optionally("GenreKeyword")\
    .optionally("RolePlayKeyword")\
    .build()

no_favorite_video_intent = IntentBuilder("NoFavoriteVideoIntent")\
    .require("FavoriteVideoContext")\
    .require("NoKeyword")\
    .build()

watch_favorite_video_intent = IntentBuilder("WatchFavoriteVideoIntent")\
    .require("WatchFavoriteVideoContext")\
    .require("YesKeyword")\
    .optionally("GenreKeyword")\
    .optionally("RolePlayKeyword")\
    .build()

no_watch_favorite_video_intent = IntentBuilder("NoWatchFavoriteVideoIntent")\
    .require("WatchFavoriteVideoContext")\
    .require("NoKeyword")\
    .build()

yes_role_play_video_intent = IntentBuilder("YesRolePlayVideoIntent")\
    .require("RolePlayContext")\
    .require("YesKeyword")\
    .optionally("RolePlayKeyword")\
    .build()

no_role_play_video_intent = IntentBuilder("NoRolePlayVideoIntent")\
    .require("RolePlayContext")\
    .require("NoKeyword")\
    .build()

role_play_genre_intent = IntentBuilder("RolePlayGenreIntent")\
    .require("RolePlayGenreContext")\
    .optionally("RolePlayKeyword")\
    .build()

no_role_play_genre_intent = IntentBuilder("NoRolePlayGenreIntent")\
    .require("RolePlayGenreContext")\
    .require("NoKeyword")\
    .build()

yes_trigger_video_intent = IntentBuilder("YesTriggerVideoIntent")\
    .require("TriggerSampleContext")\
    .require("YesKeyword")\
    .optionally("GenreKeyword")\
    .build()

no_trigger_video_intent = IntentBuilder("NoTriggerVideoIntent")\
    .require("TriggerSampleContext")\
    .require("NoKeyword")\
    .build()

yes_nails_trigger_intent = IntentBuilder("YesNailsVideoIntent")\
    .require("NailTappingVideo")\
    .require("YesKeyword")\
    .build()

no_nails_trigger_intent = IntentBuilder("NoNailsVideoIntent")\
    .require("NailTappingVideo")\
    .require("NoKeyword")\
    .build()



# Regular entity groups
entities = {
    'ExitKeyword': exit_keywords,
    'MenuKeyword': menu_keywords, 
    'SearchKeyword': search_keywords,
    'VideoKeyword': video_keywords,
    'AsmrKeyword': asmr_keywords,
    'GenreKeyword': genre_keywords,
    'RolePlayKeyword': roleplay_keywords,
    'ThanksKeyword': thanks_keywords,
    'PleaseKeyword': please_keywords,
    'NoKeyword': no_keywords,
    'YesKeyword': yes_keywords,
    'AboutKeyword': about_keywords
}

# List of lists of regular expression entities
#multi_regex_entities = [todo_regex_keywords, appointment_regex_keywords,
                        #entry_regex_keywords]
# List of regular expression entity strings
single_regex_entities = [with_regex_keyword]

skill_intents = [search_intent, menu_intent, favorite_video_intent,yes_favorite_video_intent,  no_favorite_video_intent, watch_favorite_video_intent, no_watch_favorite_video_intent, yes_role_play_video_intent, no_role_play_video_intent, role_play_genre_intent, no_role_play_genre_intent, yes_trigger_video_intent, no_trigger_video_intent, yes_nails_trigger_intent, no_nails_trigger_intent, about_asmr_intent, quit_intent]

