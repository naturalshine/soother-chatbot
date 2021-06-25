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
		response = ""

		"""
		Chooses proper action to take based on intent.

		:param dict intent: 

		"""


		intent_type = intent['intent_type']
		cherrypy.log(intent_type)
		if intent_type == 'AboutAsmrIntent':
			self.ContextManager.handle_add_context("AsmrContext")
			response = "ASMR, Autonomous Sensory Meridian Response, describes a tingling sensation in the scalp and spine in response to soft sounds like whispering, nail-tapping, and hair-brushing."
		elif intent_type == 'TriggerIntent':
			response = "ASMR triggers tend to be soft sounds produced by everyday objects. Some favorites include fizzing liquids, sugar poured into water, nail polish bottles clacking together, and the sound of a marker on paper."
		elif intent_type == 'TherapyIntent':
			response = "Many people watch ASMR videos for the calming effects of the slow and soft sounds. Content of ASMR videos is often focused on relieving insomnia and anxiety."

		elif intent_type == 'HistoryIntent':
			response = "ASMR was given its name in a Yahoo forum in 2008. From the early 2010s, it gained momentum as a cultural phenomnenon on Youtube, where ASMRtists have posted millions of videos designed to tigger the sensation."

		elif intent_type == 'ExampleIntent':
			NewBrain = Brain()
			text = "asmr example video"
			r = NewBrain.handle_from_skill(text)
			r['response'] = "Here's an example ASMR video."
			cherrypy.session["activeSkill"] = ""
			response = r
		elif intent_type == 'QuitIntent':
			self.ContextManager.clear_context()
			cherrypy.lib.sessions.expire()
			response = f"BITCH BYE!!"

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

