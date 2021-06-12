#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import requests
import cherrypy

from Skill import Skill
from adapt.engine import IntentDeterminationEngine
from adapt.context import ContextManager
from padatious import IntentContainer

from .intents import (entities, single_regex_entities, intents)
from .services import SootherContextManager 



teaContextManager = SootherContextManager()


# Create adapt engine
def create_engine():
	"""
	Returns an Adapt engine.
	"""
	cherrypy.log("ENGINE")
	engine = IntentDeterminationEngine()
	# Register entities on engine
	for entity, keywords in entities.items():
		cherrypy.log("keywords")
		for keyword in keywords:
			cherrypy.log(keyword)
			engine.register_entity(keyword, entity)


	for entity in single_regex_entities:
		engine.register_regex_entity(entity)

	# Register intents on engine
	for intent in intents:
		cherrypy.log('intent')
		engine.register_intent_parser(intent)

	return engine




class tea_skill(Skill):

	def __init__(self, root_dir, name, nlp, active, hasContext):
		hasContext = True
		super(tea_skill, self).__init__(root_dir, name, nlp, active, hasContext)

	def act_on_intent(self, intent):
		response = ""

		"""
		Chooses proper action to take based on intent.

		:param dict intent: 

		"""
		cherrypy.log("ACT ON INTENT")

		intent_type = intent['intent_type']
		cherrypy.log(intent_type)
		if intent_type == 'BringTeaIntent':
			teaContextManager.handle_add_context('TeaContext')
			response = "What kind of tea?"

		elif intent_type == 'YesHoneyIntent':
			teaContextManager.remove_context('HoneyContext')			
			teaContextManager.handle_add_context('EndContext')
			response = "BITCH TAKE YOUR TEA AND SHOVE IT DOWN YOUR PUSSSY"

		elif intent_type == 'NoHoneyIntent':
			teaContextManager.remove_context('HoneyContext')
			teaContextManager.handle_add_context('EndContext')
			response = "BITCH NO TEA FOR YOU"

		elif intent_type == 'YesMilkIntent':
			teaContextManager.remove_context('MilkContext')
			teaContextManager.handle_add_context('HoneyContext')
			response = "HOW ABOUT HONEY BITCH"

		elif intent_type == 'NoMilkIntent':
			teaContextManager.remove_context('MilkContext')			
			teaContextManager.handle_add_context('HoneyContext')
			response = "NO MILK BUT HONEY????"

		elif intent_type == 'TeaTypeIntent':
			teaContextManager.remove_context('TeaContext')
			teaContextManager.handle_add_context('MilkContext')
			response = "Sure, do you want milk?"

		elif intent_type == 'NoTeaTypeIntent':
			teaContextManager.remove_context('TeaContext')			
			teaContextManager.handle_add_context('MilkContext')
			response = "Sure, green tea it will be. Do you want milk?"

		elif intent_type == 'WelcomeIntent':
			teaContextManager.remove_context('EndContext')
			cherrypy.lib.sessions.expire()
			response = "You're welcome!!"
		else: 
			teaContextManager.remove_context('EndContext')
			cherrypy.lib.sessions.expire()
			response = "Goodbye!"

		return response

	def run_intent(self, text):
		cherrypy.log("run intent")
		engine = create_engine()
		# determine intents in text
		intents = [intent for intent in engine.determine_intent(text, include_tags=True, context_manager=teaContextManager)]
		#cherrypy.log(intents)
		cherrypy.log("^^^^^^^ INTENTS")
		responseArr = []

		# if there are intents in the text
		if intents:
			cherrypy.log("INTENTSx2")
			# act on them
			# this should only be one for our usecase
			for intent in intents:
				cherrypy.log('intent of intents')
				response = self.act_on_intent(intent)
				responseArr.append(response)

		return responseArr

	def handle(self, intent_parser_result, text, latitude, longitude):
		cherrypy.log("hi")

		skill_response = []
		context = intent_parser_result.matches

		skill_response = self.run_intent(text)
		cherrypy.log("SKILL RESPONSE ")
		for skill in skill_response:
			cherrypy.log(skill)
		return skill_response

		'''
		finalString = ""

		for key, value in context.items():
			cherrypy.log("HELLOOOOO")
			context[key] = context[key].replace("?","")
			finalString += context[key]
			cherrypy.log(finalString)
			cherrypy.log(value)
		
		cherrypy.log(context["keyword"])
		'''
		'''
		skill_response.append({
			'title': actions,
			'description': "",
			'url': ""})
		'''
		'''
		else:
			skill_response.append({
				'title':'',
				'description':'Sorry we couldn\'t find %s on Youtube!' % context["keyword"],
				'url':''})
		'''

