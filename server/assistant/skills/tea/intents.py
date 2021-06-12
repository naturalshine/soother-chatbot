#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module creates intent parsers for the adapt engine.
"""
from adapt.intent import IntentBuilder


# General purpose keywords
bring_keywords = [
    'want',
    'would like',
    'to have',
    'have',
    'drink',
    'bring',
    'serve',
    'take',
    'create',
    'make'
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

tea_type_keywords = [
    'green',
    'black',
    'white',
    'red'
]

tea_keywords = [
    'tea',
    'hot water',
    'steep',
    'infusion',
    'tee'
]

no_keywords = [
    'no',
    'nope',
    'nein',
    'naw'
]
yes_keywords = [
    'yes',
    'ya',
    'yeah',
    'ja'
]

no_preference_keywords = [
    'don\'t care',
    'any',
    'whatever',
    'matter'
]

milk_keywords = [
    'milk',
    'white',
    'non-dairy',
    'cream'
]

honey_keywords = [
    'honey',
    'sweet',
    'sweetened',
    'sweeten',
    'sweetener',
    'bee'
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
bring_tea_intent = IntentBuilder('BringTeaIntent')\
    .require('BringKeyword')\
    .require('TeaKeyword')\
    .optionally('SelfKeyword')\
    .optionally('PleaseKeyword')\
    .build()

no_tea_intent = IntentBuilder('NoTeaIntent')\
    .require('NoKeyword')\
    .optionally('ThanksKeyword')\
    .optionally('SelfKeyword')\
    .build()

tea_type_intent = IntentBuilder('TeaTypeIntent')\
    .require('TeaContext')\
    .require('TeaTypeKeyword')\
    .optionally('PleaseKeyword')\
    .build()

no_tea_type_intent = IntentBuilder('NoTeaTypeIntent')\
    .require('TeaContext')\
    .require('NoPreferenceKeyword')\
    .optionally('SelfKeyword')\
    .build()

yes_milk_intent = IntentBuilder('YesMilkIntent')\
    .require('MilkContext')\
    .require('YesKeyword')\
    .optionally('PleaseKeyword')\
    .build()

no_milk_intent = IntentBuilder('NoMilkIntent')\
    .require('MilkContext')\
    .require('NoKeyword')\
    .optionally('With')\
    .optionally('ThanksKeyword')\
    .build()

yes_honey_intent = IntentBuilder('YesHoneyIntent')\
    .require('HoneyContext')\
    .require('YesKeyword')\
    .optionally('With')\
    .optionally('PleaseKeyword')\
    .build()

no_honey_intent = IntentBuilder('NoHoneyIntent')\
    .require('HoneyContext')\
    .require('NoKeyword')\
    .optionally('ThanksKeyword')\
    .build()

welcome_intent = IntentBuilder('WelcomeIntent')\
    .require('EndContext')\
    .require('ThanksKeyword')\
    .build()


# Regular entity groups
entities = {
    'YesKeyword': yes_keywords,
    'BringKeyword': bring_keywords,
    'NoKeyword': no_keywords,
    'TeaKeyword': tea_keywords,
    'TeaTypeKeyword': tea_type_keywords,
    'HoneyKeyword': honey_keywords,
    'MilkKeyword': milk_keywords,
    'ThanksKeyword': thanks_keywords,
    'PleaseKeyword': please_keywords,
    'SelfKeyword': self_keywords,
    'NoPreferenceKeyword': no_preference_keywords
}
# List of lists of regular expression entities
#multi_regex_entities = [todo_regex_keywords, appointment_regex_keywords,
                        #entry_regex_keywords]
# List of regular expression entity strings
single_regex_entities = [with_regex_keyword]

intents = [bring_tea_intent, yes_honey_intent,
           no_honey_intent, yes_milk_intent, no_milk_intent, 
           tea_type_intent, no_tea_type_intent, welcome_intent]

