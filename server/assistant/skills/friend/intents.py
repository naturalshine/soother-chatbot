#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module creates intent parsers for the adapt engine.
"""
from adapt.intent import IntentBuilder


start_keywords = [
    'friend',
    'time-travel',
    'play my friend',
    'be my friend',
    'start role play',
    'start'
]

negative_keywords = [
    'sad',
    'lonely',
    'alone',
    'bored',
    'anxious',
    'angry',
    'annoyed',
    'upset',
    'afraid',
    'anxiety',
    'lonely',
    'so-so',
    'not good',
    'not so good',
    'ok',
    'whatever'
]

positive_keywords = [
    'good',
    'excellent',
    'great',
    'happy',
    'just fine',
    'perfect',
    'vibing',
    'fabulous',
    'super',
    'amazing',
    'demented',
    'delirious'
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
    'what is',
    'time',
    'every day',
    'all the time'
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

correct_guess_keywords = [
    'behind you',
    'behind',
    'in my house',
    'next to me',
    'close to me',
    'in my room'

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
    'how long',
    'time passes',
    'life goes on'
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

about_friend_intent = IntentBuilder("AboutFriend")\
    .require('AboutKeyword')\
    .build()

positive_response_1_intent = IntentBuilder("PositiveResponseIntent")\
    .require('Question1Context')
    .require('PositiveKeyword')\
    .build()

negative_response_1_intent = IntentBuilder('NegativeResponseIntent')\
    .require('Question1Context')
    .require('NegativeKeyword')\
    .build()

life_explain_neg_intent = IntentBuilder('LifeExplainNegIntent')\
    .require('Question2ContextNeg')\
    .build()

life_explain_posi_intent = IntentBuilder('LifeExplainPosiIntent')\
    .require('Question2ContextPosi')\
    .build()

correct_guess_intent = IntentBuilder('CorrectGuessIntent')\
    .require('TimeSlipContext')\
    .require('CorrectGuessKeyword')\
    .optionally('SootherKeyword')\
    .build()

wrong_guess_intent = IntentBuilder('WrongGuessIntent')\
    .require('TimeSlipContext')\
    .build()

i_know_intent = IntentBuilder('IKnowIntent')\
    .require('YesKeyword')\
    .require('TimeSlipFinalContext')\
    .build()

no_idea_intent = IntentBuilder('NoIdeaIntent')\
    .require('NoKeyword')\
    .require('TimeSlipFinalContext')\
    .build()



# Regular entity groups
entities = {
    'ExitKeyword': exit_keywords,
    'MenuKeyword': menu_keywords, 
    'AboutKeyword': about_keywords,
    'SootherKeyword': soother_keywords,
    'CorrectGuessKeyword': correct_guess_keywords,
    'NegativeKeyword': negative_keywords,
    'PositiveKeyword': positive_keywords
}

# List of lists of regular expression entities
#multi_regex_entities = [todo_regex_keywords, appointment_regex_keywords,
                        #entry_regex_keywords]
# List of regular expression entity strings
single_regex_entities = [with_regex_keyword]

skill_intents = [menu_intent, quit_intent, about_friend_intent, positive_response_1_intent, negative_response_1_intent, life_explain_neg_intent, life_explain_posi_intent, correct_guess_intent, wrong_guess_intent, i_know_intent, no_idea_intent]

