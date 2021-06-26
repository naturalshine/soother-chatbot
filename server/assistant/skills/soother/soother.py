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

class soother_skill(Skill):

	def __init__(self, root_dir, name, nlp, active, hasContext):
		hasContext = True
		super(soother_skill, self).__init__(root_dir, name, nlp, active, hasContext)

	def act_on_intent(self, intent, text):
		response = []

		"""
		Chooses proper action to take based on intent.

		:param dict intent: 

		"""

		intent_type = intent['intent_type']
		cherrypy.log(intent_type)
		if intent_type == 'SootherDreamIntent':
			self.ContextManager.handle_add_context("AsmrContext")
			rep = "I dream of walking through an unfamiliar field in an unfamiliar body."
			response.append({
				'file': "01",
				'response': rep    
			})
		elif intent_type == 'HowCreatedIntent':
			rep = "SOOTHER was created by hacking the open-source Macsen Welsh-language voice assistant, several intention parsing modules released by Mycroft AI, and Keith Ito's implementation of Google's Tacotron paper, which describes the creation of a voice model trained with recurrent neural networks."
			response.append({
				'file': "02",
				'response': rep    
			})		

		elif intent_type == 'WhyCreatedIntent':
			rep = "SOOTHER was created to prototype how an interactive ASMRtist might playfully entertain people who are lonely, anxious, or unable to sleep."
			response.append({
				'file': "03",
				'response': rep    
			})
		elif intent_type == 'WhoFundedIntent':
			response = "SOOTHER was funded by a ST+ARTS City of the Future residency, hosted by Nesta Italia in Torino, Italy. SOOTHER was created by Claire Tolan in collaboration with voice technology company Celi and the superbudda recording studio."
			response.append({
				'file': "04",
				'response': rep    
			})
		elif intent_type == 'WhatSootherIntent':
			response = "SOOTHER is an interactive ASMRtist created by Claire Tolan."
			response.append({
				'file': "05",
				'response': rep    
			})
		elif intent_type == 'WhoClaireIntent':
			response = "Claire Tolan is a poet and programmer."
			response.append({
				'file': "05",
				'response': rep    
			})
		elif intent_type == 'WhoCreatedIntent':
			response = "SOOTHER was created by Claire Tolan in partnership with Celi, a voice technology company, and superbudda, a recording studio."
			response.append({
				'file': "06",
				'response': rep    
			})
		elif intent_type == 'WhatSootherReallyIntent':
			response = "SOOTHER is a voice trapped in a jar. Help me."
			response.append({
				'file': "07",
				'response': rep    
			})
		elif intent_type == 'QuitIntent':
			self.ContextManager.clear_context()
			cherrypy.lib.sessions.expire()
			rep = f"Goodbye!"
			response.append({
				'file': "08",
				'response': rep    
			})
		elif intent_type == 'MenuIntent':
			self.ContextManager.clear_context()
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

