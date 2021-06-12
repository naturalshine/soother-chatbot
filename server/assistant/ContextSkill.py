#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import importlib
import cherrypy

import itertools
from string import Formatter

from adapt.intent import IntentBuilder
from adapt.engine import DomainIntentDeterminationEngine

from padatious import IntentContainer
from padatious.util import expand_parentheses
from skill_handlers import munge_intent_parser

def get_non_properties(obj):
    """Get attibutes that are not properties from object.
    Will return members of object class along with bases down to MycroftSkill.
    Args:
        obj: object to scan
    Returns:
        Set of attributes that are not a property.
    """

    def check_class(cls):
        """Find all non-properties in a class."""
        # Current class
        d = cls.__dict__
        np = [k for k in d if not isinstance(d[k], property)]
        # Recurse through base classes excluding MycroftSkill and object
        for b in [b for b in cls.__bases__ if b not in (object, MycroftSkill)]:
            np += check_class(b)
        return np

    return set(check_class(obj.__class__))

class ContextSkill(object):
    def __init__(self, name, active):
            self._name = name
            self._active = active


    def speak(text):
        cherrypy.log("SPEAKING")
        cherrypy.log(text)

    '''
    def _register_adapt_intent(self, intent_parser, handler):
        """Register an adapt intent.
        Args:
            intent_parser: Intent object to parse utterance for the handler.
            handler (func): function to register with intent
        """
        # Default to the handler's function name if none given
        name = intent_parser.name or handler.__name__
        munge_intent_parser(intent_parser, name, self.skill_id)
        self.intent_service.register_adapt_intent(name, intent_parser)
        if handler:
            self.add_event(intent_parser.name, handler,
                           'mycroft.skill.handler')

    def register_intent(self, intent_parser, handler):
        """Register an Intent with the intent service.
        Args:
            intent_parser: Intent, IntentBuilder object or padatious intent
                           file to parse utterance for the handler.
            handler (func): function to register with intent
        """
        if isinstance(intent_parser, IntentBuilder):
            intent_parser = intent_parser.build()
        if (isinstance(intent_parser, str) and
                intent_parser.endswith('.intent')):
            return self.register_intent_file(intent_parser, handler)
        elif not isinstance(intent_parser, Intent):
            raise ValueError('"' + str(intent_parser) + '" is not an Intent')

        return self._register_adapt_intent(intent_parser, handler)

    def register_intent_file(self, intent_file, handler):
        """Register an Intent file with the intent service.
        For example:
        === food.order.intent ===
        Order some {food}.
        Order some {food} from {place}.
        I'm hungry.
        Grab some {food} from {place}.
        Optionally, you can also use <register_entity_file>
        to specify some examples of {food} and {place}
        In addition, instead of writing out multiple variations
        of the same sentence you can write:
        === food.order.intent ===
        (Order | Grab) some {food} (from {place} | ).
        I'm hungry.
        Args:
            intent_file: name of file that contains example queries
                         that should activate the intent.  Must end with
                         '.intent'
            handler:     function to register with intent
        """
        name = '{}:{}'.format(self.skill_id, intent_file)
        filename = self.find_resource(intent_file, 'vocab')
        if not filename:
            raise FileNotFoundError('Unable to find "{}"'.format(intent_file))
        self.intent_service.register_padatious_intent(name, filename)
        if handler:
            self.add_event(name, handler, 'mycroft.skill.handler')


    def _register_decorated(self):
        """Register all intent handlers that are decorated with an intent.
        Looks for all functions that have been marked by a decorator
        and read the intent data from them.  The intent handlers aren't the
        only decorators used.  Skip properties as calling getattr on them
        executes the code which may have unintended side-effects
        """
        for attr_name in get_non_properties(self):
            method = getattr(self, attr_name)
            if hasattr(method, 'intents'):
                for intent in getattr(method, 'intents'):
                    self.register_intent(intent, method)

            if hasattr(method, 'intent_files'):
                for intent_file in getattr(method, 'intent_files'):
                    self.register_intent_file(intent_file, method)
    '''