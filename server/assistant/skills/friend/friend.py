#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import requests
import cherrypy
import random

from padatious import IntentContainer
from adapt.engine import IntentDeterminationEngine

from Skill import Skill
from Brain import Brain
from .intents import (entities, single_regex_entities, skill_intents)


class friend_skill(Skill):

	def __init__(self, root_dir, name, nlp, active, hasContext):
		hasContext = True
		super(friend_skill, self).__init__(root_dir, name, nlp, active, hasContext)

	def act_on_intent(self, intent, text):
		response = []
		

		"""
		Chooses proper action to take based on intent.

		:param dict intent: 

		"""
		cherrypy.log("ACT ON INTENT")

		intent_type = intent['intent_type']
		cherrypy.log(intent_type)
		if intent_type == 'AboutFriend':
			self.ContextManager.clear_context()
			rep = "I slip through time, it cannot be stopped. You know what it's like. You gave me my radio when I slid into your treehouse years ago. You're my only stable contact, and I'm so thankful you're here."
			response.append({
				'file': "01",
				'response': rep    
			})
		elif intent_type == 'StartIntent':
			self.ContextManager.clear_context()
			self.ContextManager.handle_add_context("Question1Context")
			rep = "Shhhh is that you my friend? Shhhh There's a lot of static on the line. Shhhh. How are you today? Over."
			response.append({
				'file': "02",
				'response': rep    
			})
		elif intent_type == 'PositiveResponseIntent':
			self.ContextManager.remove_context("Question1Context")
			self.ContextManager.handle_add_context("PositiveContext")
			rep = "Ah, I'm glad to hear that my friend. Shhhhh. I'm feeling really down. I've been bouncing between 14th century Florence and some smoky techno club in circa 2005 Berlin the past few hours. I've got a killer migraine. Shhhhh. Do you have fun plans today? Shhhh. Over."
			response.append({
				'file': "03",
				'response': rep    
			})

		elif intent_type == 'NegativeResponseIntent':
			self.ContextManager.remove_context("Question1Context")
			self.ContextManager.handle_add_context("NegativeContext")
			rep = "I'm sorry to hear that my friend. Shhhh. For sure life is hard even for those who are anchored in time. Perhaps even harder. I flit between the centuries sticking to nothing and no one. Shhh. Right now I'm in the wilderness. I'm trying to identify the epoch by the flora. Shhh. Maybe Triassic? I know it doesn't matter. But I sometimes think it is the only thing that will keep me sane. Shhhh. Did you have a bad day at work? Shhh. Over."
			response.append({
				'file': "04",
				'response': rep    
			})

		elif intent_type == 'LifeExplainNegIntent':
			self.ContextManager.remove_context("NegativeContext")
			self.ContextManager.handle_add_context("TimeSlipContext")
			rep = "Shhhh. Ah my friend that sounds tough. Shhhh. I wish I could give you a hug. But that hasn't happened for how many years? Shhh. My friend it's happening again. Shhhhhh. I'm slipping. Shhhh. Time is flashing by. Shhhhh. Days and hours and minutes etched like a fractal before me. The fabric of the universe unwoven. Shhhh. Oh wow. It stopped. Can you guess where I am? Shhhh. Over."
			response.append({
				'file': "05",
				'response': rep    
			})
		elif intent_type == 'LifeExplainPosiIntent':
			self.ContextManager.remove_context("PositiveContext")
			self.ContextManager.handle_add_context("TimeSlipContext")
			rep = "Ah that sounds so nice. So calm. It really brings me joy to live vicariously through your stability. Makes me feel a bit stable just to hear of your day. It's so long since we've been in the same place. Shhh. My friend it's happening again. Shhhhhh. I'm slipping. Shhhh. Time is flashing by. Shhhhh. Days and hours and minutes etched like a fractal before me. The fabric of the universe unwoven. Shhh. Oh wow. It stopped. Can you guess where I am? Over."
			response.append({
				'file': "06",
				'response': rep    
			})

		elif intent_type == 'CorrectGuessIntent':
			self.ContextManager.remove_context("TimeSlipContext")
			self.ContextManager.handle_add_context("TimeSlipFinalContext")
			rep = "How did you guess? Turn around very slowly. Do not make any sudden moves. Do you know what this means?"
			response.append({
				'file': "07",
				'response': rep    
			})

		elif intent_type == 'WrongGuessIntent':
			self.ContextManager.remove_context("TimeSlipContext")
			self.ContextManager.handle_add_context("TimeSlipFinalContext")

			rep = "There's no static. That's right. Lean into your radio. My voice is coming from somewhere else. I'm behind you! Turn around slowly. Don't make any sudden moves. Do you know what this means?"
			response.append({
				'file': "08",
				'response': rep    
			})
		elif intent_type == 'NoIdeaIntent':
			self.ContextManager.remove_context("TimeSlipFinalContext")
			self.ContextManager.clear_context()
			rep = "You don't know what it means? My friend, you can finally take my place as you promised years ago. We just need to... Shhh. Oh no. Not again. Shhhh I'm slipping."
			response.append({
				'file': "09",
				'response': rep    
			})
		elif intent_type == 'IKnowIntent':
			self.ContextManager.remove_context("TimeSlipFinalContext")
			self.ContextManager.clear_context()
			rep = "Then you remember the promise you made to me years ago. That you would take my place. We just need to... Shhh. Oh no. Not again. Shhhh I'm slipping."
			response.append({
				'file': "10",
				'response': rep    
			})
		elif intent_type == 'QuitIntent':
			self.ContextManager.clear_context()
			cherrypy.lib.sessions.expire()
			rep = f"Goodbye! Over."
			response.append({
				'file': "11",
				'response': rep    
			})
		elif intent_type == 'MenuIntent':
			self.ContextManager.clear_context()
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0
			rep = "10 4. Shhhh. Lots of noise on our connection today. Shhhh. We can just chat over the radio, shhhh. Or I can tell you more about ASMR, shhhh. Tell you about SOOTHER, or recommend ASMR content. Shhh. Over."
			response.append({
				'file': "12",
				'response': rep    
			})

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

