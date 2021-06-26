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

class Menu_skill(Skill):

	def __init__(self, root_dir, name, nlp, active, hasContext):
		hasContext = True		
		super(Menu_skill, self).__init__(root_dir, name, nlp, active, hasContext)

	def act_on_intent(self, intent, text):
		response = []

		"""
		Chooses proper action to take based on intent.

		:param dict intent: 

		"""

		intent_type = intent['intent_type']
		cherrypy.log(intent_type)
		if intent_type == 'QuitIntent':
			self.ContextManager.clear_context()
			cherrypy.lib.sessions.expire()
			rep = f"Bye!"
			response.append({
				'file': "0",
				'response': rep    
			})
		elif intent_type == 'DogMenuIntent':
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0			
			# trigger menu skill here
			menu = intent["MenuKeyword"]
			rep = "I'm your dog, I'm your therapist, here are your options: I can play your therapist, tell you more about myself, tell you about SOOTHER, or recommend ASMR content."
			response.append({
				'file': "01",
				'response': rep    
			})
		elif intent_type == 'AlienMenuIntent':
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0			
			# trigger menu skill here
			menu = intent["MenuKeyword"]
			rep = "I'm an alien, I'm on your head. Here are your options: we can have a head-sitting session, or I can tell you more about myself, tell you about SOOTHER, or recommend ASMR content."
			response.append({
				'file': "02",
				'response': rep    
			})
		elif intent_type == 'FriendMenuIntent':
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0			
			# trigger menu skill here
			menu = intent["MenuKeyword"]
			rep = "I'm your friend, I'm trapped in time. Here are your options: we can just chat over the radio, or I can tell you more about myself, tell you about SOOTHER, or recommend ASMR content."
			response.append({
				'file': "03",
				'response': rep    
			})
		cherrypy.session["LastUtterance"] = response
		return response


	def handle(self, text):

		skill_response = []

		context = cherrypy.session.get("RolePlayContext")
		cherrypy.log("CONTEXT")
		cherrypy.log(context)
		cherrypy.log(cherrypy.session["RolePlayContext"])
		self.ContextManager.handle_add_context(context)

		contextLst = []
		#self.ContextManager.clear_context()
		contextLst = self.ContextManager.get_context()
		cherrypy.log("CONTEX TLIST")
		for ct in contextLst:
			cherrypy.log(ct["key"])

		engineEntities = {"entities" : entities, "single_regex_entities" : single_regex_entities, "skill_intents": skill_intents}
		
		skill_response = self.run_intent(text, engineEntities)

		return skill_response

