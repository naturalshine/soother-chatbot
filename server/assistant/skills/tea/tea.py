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
		response = []
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
			rep = "What kind of tea?"
			response.append({
				'file': "01",
				'response': rep    
			})
		elif intent_type == 'YesHoneyIntent':
			self.ContextManager.remove_context('HoneyContext')			
			self.ContextManager.handle_add_context('EndContext')
			honey = True
			if milk:
				rep = f"Sure, here's some {teaType} tea with milk and honey"
				response.append({
					'file': "02",
					'response': rep    
				})
			else: 
				rep = f"Here's youre {teaType} tea with honey but no milk"
				response.append({
					'file': "03",
					'response': rep    
				})
		elif intent_type == 'NoHoneyIntent':
			self.ContextManager.remove_context('HoneyContext')
			self.ContextManager.handle_add_context('EndContext')
			honey = False
			if milk:
				rep = f"Here's your {teaType} tea with milk and no honey."
				response.append({
					'file': "04",
					'response': rep    
				})
			else: 
				rep = f"Here's your {teaType} tea without milk and honey"
				response.append({
					'file': "05",
					'response': rep    
				})
		elif intent_type == 'YesMilkIntent':
			self.ContextManager.remove_context('MilkContext')
			self.ContextManager.handle_add_context('HoneyContext')
			milk = True
			rep = "How about honey?"
			response.append({
				'file': "06",
				'response': rep    
			})
		elif intent_type == 'NoMilkIntent':
			self.ContextManager.remove_context('MilkContext')			
			self.ContextManager.handle_add_context('HoneyContext')
			milk = False
			rep = "No milk, but honey?"
			response.append({
				'file': "07",
				'response': rep    
			})
		elif intent_type == 'TeaTypeIntent':
			self.ContextManager.remove_context('TeaContext')
			self.ContextManager.handle_add_context('MilkContext')
			teaType = intent["TeaTypeKeyword"]
			rep = "Sure, do you want milk?"
			response.append({
				'file': "08",
				'response': rep    
			})
		elif intent_type == 'NoTeaTypeIntent':
			self.ContextManager.remove_context('TeaContext')			
			self.ContextManager.handle_add_context('MilkContext')
			rep = "Sure, green tea it will be. Do you want milk?"
			response.append({
				'file': "09",
				'response': rep    
			})
		elif intent_type == 'WelcomeIntent':
			self.ContextManager.clear_context()
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0			
			rep = f"You're welcome!! Enjoy your {teaType} tea"
			response.append({
				'file': "10",
				'response': rep    
			})
		elif intent_type == 'QuitIntent':
			self.ContextManager.clear_context()
			cherrypy.lib.sessions.expire()
			rep = f"Bye! Enjoy your {teaType} tea"
			response.append({
				'file': "11",
				'response': rep    
			})
		elif intent_type == 'MenuIntent':
			self.ContextManager.clear_context()
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0
			print(cherrypy.session["RolePlayContext"])
			# trigger menu skill here
			menu = intent["MenuKeyword"]
			NewBrain = Brain()
			response = NewBrain.handle_from_skill(text)

		cherrypy.session["LastUtterance"] = response
		return response


	def handle(self, text, **kwargs):
		cherrypy.log("hi")

		skill_response = []


		contextLst = []
		contextLst = self.ContextManager.get_context()
		cherrypy.log("CONTEX TLIST")
		for ct in contextLst:
			cherrypy.log(ct["key"])
		engineEntities = {"entities" : entities, "single_regex_entities" : single_regex_entities, "skill_intents": skill_intents}

		skill_response = self.run_intent(text, engineEntities)

		return skill_response

