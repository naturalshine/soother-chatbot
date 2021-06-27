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
			menu = intent["MenuKeyword"]
			rep = "We can have a therapy session, or I can tell you more about ASMR, tell you about SOOTHER, or recommend ASMR content. RuffRuff. Excuse me. RuffRuff. Someone's at the door. RuffRuff."
			response.append({
				'file': "01",
				'response': rep    
			})
		elif intent_type == 'AlienMenuIntent':
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0			
			menu = intent["MenuKeyword"]
			rep = "Let me query my tentacles. I'm told these are the options: I can guide you through a meditation. Or I can tell you more about ASMR, tell you about SOOTHER, or recommend ASMR content."
			response.append({
				'file': "02",
				'response': rep    
			})
		elif intent_type == 'FriendMenuIntent':
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0			
			menu = intent["MenuKeyword"]
			rep = "10 4. Shhhh. Lots of noise on our connection today. Shhhh. We can just chat over the radio, shhhh. Or I can tell you more about ASMR, shhhh. Tell you about SOOTHER, or recommend ASMR content. Shhh. Over."
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

