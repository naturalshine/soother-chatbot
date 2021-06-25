#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import requests
import cherrypy
from padatious import IntentContainer
from adapt.engine import IntentDeterminationEngine

from Skill import Skill
from Brain import Brain
from .intents import (entities, single_regex_entities, skill_intents)


class tea_skill(Skill):

	def __init__(self, root_dir, name, nlp, active, hasContext):
		hasContext = True
		super(tea_skill, self).__init__(root_dir, name, nlp, active, hasContext)

	def act_on_intent(self, intent, text):
		response = ""
		milk = False
		honey = False
		teaType = "green"

		"""
		Chooses proper action to take based on intent.

		:param dict intent: 

		"""
		cherrypy.log("ACT ON INTENT")


		intent_type = intent['intent_type']
		cherrypy.log(intent_type)
		if intent_type == 'BringTeaIntent':
			self.ContextManager.handle_add_context('TeaContext')
			response = "What kind of tea?"

		elif intent_type == 'YesHoneyIntent':
			self.ContextManager.remove_context('HoneyContext')			
			self.ContextManager.handle_add_context('EndContext')
			honey = True
			if milk:
				response = f"BITCH TAKE YOUR {teaType} TEA with milk and honey AND SHOVE IT DOWN YOUR PUSSSY"
			else: 
				response = f"BITCH TAKE YOUR {teaType} TEA with honey and no milk AND SHOVE IT DOWN YOUR PUSSSY"

		elif intent_type == 'NoHoneyIntent':
			self.ContextManager.remove_context('HoneyContext')
			self.ContextManager.handle_add_context('EndContext')
			honey = False
			if milk:
				response = f"BITCH here's your {teaType} tea with milk and no honey."
			else: 
				response = f"Bitch here's your {teaType} tea without milk and honey"

		elif intent_type == 'YesMilkIntent':
			self.ContextManager.remove_context('MilkContext')
			self.ContextManager.handle_add_context('HoneyContext')
			milk = True
			response = "HOW ABOUT HONEY BITCH"

		elif intent_type == 'NoMilkIntent':
			self.ContextManager.remove_context('MilkContext')			
			self.ContextManager.handle_add_context('HoneyContext')
			milk = False
			response = "NO MILK BUT HONEY????"

		elif intent_type == 'TeaTypeIntent':
			self.ContextManager.remove_context('TeaContext')
			self.ContextManager.handle_add_context('MilkContext')
			teaType = intent["TeaTypeKeyword"]
			response = "Sure, do you want milk?"

		elif intent_type == 'NoTeaTypeIntent':
			self.ContextManager.remove_context('TeaContext')			
			self.ContextManager.handle_add_context('MilkContext')
			response = "Sure, green tea it will be. Do you want milk?"

		elif intent_type == 'WelcomeIntent':
			self.ContextManager.clear_context()
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0			
			response = f"You're welcome!! Enjoy your {teaType} tea"
		
		elif intent_type == 'QuitIntent':
			self.ContextManager.clear_context()
			cherrypy.lib.sessions.expire()
			response = f"BITCH BYE!! Shove your {teaType} tea"

		elif intent_type == 'MenuIntent':
			self.ContextManager.clear_context()
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0
			# trigger menu skill here
			menu = intent["MenuKeyword"]
			NewBrain = Brain()
			response = NewBrain.handle_from_skill(text)

		cherrypy.session["LastUtterance"] = response
		return response


	def handle(self, text, **kwargs):
		cherrypy.log("hi")

		skill_response = []

		engineEntities = {"entities" : entities, "single_regex_entities" : single_regex_entities, "skill_intents": skill_intents}

		skill_response = self.run_intent(text, engineEntities)

		return skill_response

