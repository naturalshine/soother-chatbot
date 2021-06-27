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


class dog_skill(Skill):

	def __init__(self, root_dir, name, nlp, active, hasContext):
		hasContext = True
		super(dog_skill, self).__init__(root_dir, name, nlp, active, hasContext)

	def act_on_intent(self, intent, text):
		response = []
		

		"""
		Chooses proper action to take based on intent.

		:param dict intent: 

		"""
		cherrypy.log("ACT ON INTENT")

		intent_type = intent['intent_type']
		cherrypy.log(intent_type)
		if intent_type == 'AboutDog':
			rep = "I acquired language after my mommy saw Bunny the dog on TikTok and gave me a keyboard. I've earned several degrees from accredited institutions online, recently completing my MPhil/PhD in Psychoanalytic Studies. I'm a licensed analyst. On the internet, no one knows you're a dog! Now tell me about yourself."
			response.append({
				'file': "01",
				'response': rep    
			})
		elif intent_type == 'StartIntent':
			rep = "Welcome. I hope you feel comfortable. I'm Dr. RuffRuff but you can call me Ralph. What would you like to talk about today?"
			response.append({
				'file': "0",
				'response': rep    
			})
		elif intent_type == 'TherapyIntent':
			therapyKeyword = intent["TherapyKeyword"]
			sentences = [
				{	
					"file": "02",
					"text":"Does that trouble you?",
				},
				{
					"file": "03",
					"text": "Tell me more about such feelings."
				},
				{ 	"file": "04", 
					"text": f"Why can't you {therapyKeyword}"
				},
				{
					"file": "05",
					"text": "What else comes to mind when you ask that?"
				},
				{
					"file": "06",
					"text": "Have you asked such questions before?"
				},
				{
					"file": "07",
					"text": "Don't be so defensive!"
				},
				{
					"file": "08",
					"text": "You see a resemblence here? Interesting. Care to go deeper with that?"
				}
			]

			sel = random.choice(sentences)

			response.append({
				'file': sel["file"],
				'response': sel["text"]    
			})

		elif intent_type == 'ExistentialIntent':
			therapyKeyword = intent["ExistentialKeyword"]
			sentences = [
				{	
					"file": "09",
					"text":"In what way?",
				},
				{
					"file": "10",
					"text": "Let's take a moment here. Think about what you just said and try to rephrase it a bit more specifically."
				},
				{ 	"file": "11", 
					"text": "Would you say that you have psychological problems?"
				},
				{
					"file": "12",
					"text": f"But you are not sure you {therapyKeyword}"
				},
				{
					"file": "13",
					"text": "In what way?"
				},
				{
					"file": "14",
					"text": "Can you think of a specific example?"
				},
				{
					"file": "15",
					"text": f"What about your own {therapyKeyword}?"
				}
			]

			sel = random.choice(sentences)

			response.append({
				'file': sel["file"],
				'response': sel["text"]    
			})

		elif intent_type == 'FeelingIntent':
			therapyKeyword = intent["FeelingKeyword"]
			sentences = [
				{	
					"file": "16",
					"text":"Do computers make you uncomfortable?",
				},
				{
					"file": "17",
					"text": "Tell me more about such feelings."
				},
				{ 	"file": "18", 
					"text": f"Do you often feel {therapyKeyword}?"
				},
				{
					"file": "19",
					"text": f"Do you enjoy feeling {therapyKeyword}"
				},
				{
					"file": "20",
					"text": f"Did you come to me because you are {therapyKeyword}"
				},
				{
					"file": "21",
					"text": f"Do you believe it is normal to be {therapyKeyword}"
				},
				{
					"file": "22",
					"text": f"How long have you been {therapyKeyword}?"
				}
			]

			sel = random.choice(sentences)

			response.append({
				'file': sel["file"],
				'response': sel["text"]    
			})
		elif intent_type == 'HistoryIntent':
			therapyKeyword = intent["HistoryKeyword"]
			sentences = [
				{	
					"file": "23",
					"text": f"What do you mean by {therapyKeyword}?"
				},
				{
					"file": "24",
					"text": "Does time bother you?"
				},

			]

			sel = random.choice(sentences)

			response.append({
				'file': sel["file"],
				'response': sel["text"]    
			})
		elif intent_type == 'NoIntent':
			sentences = [
				{	
					"file": "25",
					"text": "That negativity isn't going to move us forward."
				},
				{
					"file": "26",
					"text": "Are you always so negative?"
				}

			]

			sel = random.choice(sentences)

			response.append({
				'file': sel["file"],
				'response': sel["text"]    
			})
		elif intent_type == 'YesIntent':
			sentences = [
				{	
					"file": "27",
					"text": "Say more about that."
				},
				{
					"file": "28",
					"text": "Could you elaborate?"
				}

			]

			sel = random.choice(sentences)

			response.append({
				'file': sel["file"],
				'response': sel["text"]    
			})
		elif intent_type == 'SootherIntent':
			sentences = [
				{	
					"file": "29",
					"text": "Do you need to make it about me because you're uncomfortable talking about yourself?"
				},
				{
					"file": "30",
					"text": "Don't blame me, I'm just a dog! What are you really saying?"
				}

			]

			sel = random.choice(sentences)

			response.append({
				'file': sel["file"],
				'response': sel["text"]    
			})
		elif intent_type == 'QuitIntent':
			self.ContextManager.clear_context()
			cherrypy.lib.sessions.expire()
			rep = f"Bye! Thanks for a great session."
			response.append({
				'file': "11",
				'response': rep    
			})
		elif intent_type == 'MenuIntent':
			self.ContextManager.clear_context()
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0
			rep = "We can have a therapy session, or I can tell you more about ASMR, tell you about SOOTHER, or recommend ASMR content. RuffRuff. Excuse me. RuffRuff. Someone's at the door. RuffRuff."
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

