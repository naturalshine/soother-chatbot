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

class Personality_skill(Skill):

	def __init__(self, root_dir, name, nlp, active, hasContext):
		hasContext = True
		super(Personality_skill, self).__init__(root_dir, name, nlp, active, hasContext)

	def act_on_intent(self, intent, text):
		response = []

		"""
		Chooses proper action to take based on intent.

		:param dict intent: 

		"""


		intent_type = intent['intent_type']
		cherrypy.log(intent_type)
		if intent_type == 'ChangeRoleIntent':
			rep = "I can play a dog who's your therapist, an alien sitting on your head, or your friend who is trapped in time. Which would you like?"
			response.append({
				'file': "0",
				'response': rep    
			})
		elif intent_type == 'RolePlayIntent':
			rep = "I can play a dog who's your therapist, an alien sitting on your head, or your friend who is trapped in time. Which would you like?"
			response.append({
				'file': "0",
				'response': rep    
			})
		elif intent_type == 'PlayDogIntent':
			cherrypy.session["RolePlayContext"] = "DogContext"
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0
			rep = "I'm your therapist and I'm a dog! What would you like to do?"
			response.append({
				'file': "01",
				'response': rep    
			})
		elif intent_type == 'PlayAlienIntent':
			cherrypy.session["RolePlayContext"] = "AlienContext"
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0
			rep = "I'm an alien and I'm sitting on your head. What would you like to do?"
			response.append({
				'file': "02",
				'response': rep    
			})
		elif intent_type == 'PlayFriendIntent':
			cherrypy.session["RolePlayContext"] = "FriendContext"
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0
			rep = "I'm your friend, I'm lost in time. What would you like to do?"
			response.append({
				'file': "03",
				'response': rep    
			})
		elif intent_type == 'QuitIntent':
			self.ContextManager.clear_context()
			cherrypy.lib.sessions.expire()
			rep = f"Goodbye!"
			response.append({
				'file': "04",
				'response': rep    
			})
		elif intent_type == 'MenuIntent':
			# trigger menu skill here
			menu = intent["MenuKeyword"]
			NewBrain = Brain()
			response = NewBrain.handle_from_skill(text)

		cherrypy.session["LastUtterance"] = response
		return response


	def handle(self, text):
		cherrypy.log("hi")

		skill_response = []

		engineEntities = {"entities" : entities, "single_regex_entities" : single_regex_entities, "skill_intents": skill_intents}

		skill_response = self.run_intent(text, engineEntities)

		return skill_response

