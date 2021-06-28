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

class asmr_skill(Skill):

	def __init__(self, root_dir, name, nlp, active, hasContext):
		hasContext = True
		super(asmr_skill, self).__init__(root_dir, name, nlp, active, hasContext)

	def act_on_intent(self, intent, text):
		response = []

		"""
		Chooses proper action to take based on intent.

		:param dict intent: 

		"""
		intent_type = intent['intent_type']
		cherrypy.log(intent_type)
		if intent_type == 'AboutAsmrIntent':
			self.ContextManager.handle_add_context("AsmrContext")
			rep = "ASMR, Autonomous Sensory Meridian Response, describes a tingling sensation in the scalp and spine. A response to soft sounds like whispering, nail-tapping, and hair-brushing."
			response.append({
				'file': "0",
				'response': rep    
			})

		elif intent_type == 'TriggerIntent':
			rep = "ASMR triggers tend to be soft sounds produced by everyday objects. Some favorites include fizzing liquids, sugar poured into water, nail polish bottles clacking together, and the sound of a marker on paper."
			response.append({
				'file': "01",
				'response': rep    
			})		
		elif intent_type == 'TherapeuticIntent':
			rep = "Many people watch ASMR videos for the calming effects of the slow and soft sounds. Content of ASMR videos is often focused on relieving insomnia and anxiety."
			response.append({
				'file': "02",
				'response': rep    
			})
		elif intent_type == 'HistoryIntent':
			rep = "ASMR was given its name in a Yahoo forum in 2008. From the early 2010s, it gained momentum as a cultural phenomnenon on Youtube, where ASMRtists have posted millions of videos designed to trigger the sensation."
			response.append({
				'file': "03",
				'response': rep    
			})
		elif intent_type == 'QuitIntent':
			self.ContextManager.clear_context()
			cherrypy.lib.sessions.expire()
			rep = f"Goodbye!"
			response.append({
				'file': "05",
				'response': rep    
			})
		elif intent_type == 'MenuIntent':
			self.ContextManager.clear_context()
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0		
			if cherrypy.session.get("RolePlayContext") == 'DogContext':
				rep = "We can have a therapy session, or I can tell you more about ASMR, tell you about SOOTHER, or recommend ASMR content. RuffRuff. Excuse me. RuffRuff. Someone's at the door. RuffRuff."
				response.append({
					'file': "menu01",
					'response': rep    
				})
			elif  cherrypy.session.get("RolePlayContext") == 'AlienContext':
				rep = "Let me query my tentacles. I'm told these are the options: I can guide you through a meditation. Or I can tell you more about ASMR, tell you about SOOTHER, or recommend ASMR content."
				response.append({
					'file': "menu02",
					'response': rep    
				})
			elif cherrypy.session.get("RolePlayContext") == 'FriendContext':
				rep = "10 4. Shhhh. Lots of noise on our connection today. Shhhh. We can just chat over the radio, shhhh. Or I can tell you more about ASMR, shhhh. Tell you about SOOTHER, or recommend ASMR content. Shhh. Over."
				response.append({
					'file': "menu03",
					'response': rep    
				})


		cherrypy.session["LastUtterance"] = response
		return response


	def handle(self, text):
		cherrypy.log("hi")

		skill_response = []

		engineEntities = {"entities" : entities, "single_regex_entities" : single_regex_entities, "skill_intents": skill_intents}

		skill_response = self.run_intent(text, engineEntities)

		return skill_response

