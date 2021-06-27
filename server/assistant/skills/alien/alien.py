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


class alien_skill(Skill):

	def __init__(self, root_dir, name, nlp, active, hasContext):
		hasContext = True
		super(alien_skill, self).__init__(root_dir, name, nlp, active, hasContext)

	def act_on_intent(self, intent, text):
		response = []
		

		"""
		Chooses proper action to take based on intent.

		:param dict intent: 

		"""
		cherrypy.log("ACT ON INTENT")

		intent_type = intent['intent_type']
		cherrypy.log(intent_type)
		if intent_type == 'AboutAlien':
			self.ContextManager.clear_context()
			self.ContextManager.handle_add_context("Question1Context")
			rep = "I am one of the Entities of the Type Ohaiglo. We are of the planet in the center of the earth. You may know our ancestors the entities of Lichen. We sit atop the heads of humans, invisible except in a birchwood, feasting on your tingles with our many tentacles. Would you like to do a meditation in a birchwood or on my home planet?"
			response.append({
				'file': "01",
				'response': rep    
			})
		elif intent_type == 'StartIntent':
			self.ContextManager.clear_context()
			self.ContextManager.handle_add_context("Question1Context")
			rep = "It is I, an entity of Ohaiglo. I sit atop your head. I can guide you through a meditation set in a birchwood or in my home planet at the center of the earth."
			response.append({
				'file': "02",
				'response': rep    
			})
		elif intent_type == 'BirchwoodFirstIntent':
			self.ContextManager.remove_context("Question1Context")
			self.ContextManager.handle_add_context("BirchwoodFirstContext")
			rep = "We are in wood of birch. Close your eyes. Visualise the trees, bending in a slight breeze, leaves rustling. Would you like full sun or partial shade?"
			response.append({
				'file': "03",
				'response': rep    
			})

		elif intent_type == 'BirchwoodSunIntent':
			self.ContextManager.remove_context("BirchwoodFirstContext")
			self.ContextManager.handle_add_context("BirchwoodSunContext")
			rep = "You lie in a clearing among the birch trees, in tall grass, among blue, red, and orange wildflowers. The sun is strong on your skin and your feel your entire body supported by cool ground. You put your jacket over your face to shade your eyes. Do you focus on sound or smell?"
			response.append({
				'file': "04",
				'response': rep    
			})

		elif intent_type == 'BirchwoodSoundIntent':
			self.ContextManager.remove_context("BirchwoodSunContext")
			rep = "It hasn't rained for a long time and everything is dry, making more sound. Along with the leaves, you hear a distant roar from the huge waterfall a kilometer away, and tinkling of a closer stream. Cicadas hum in the trees and the bushes and the trees around the clearing, their sound rising and falling in waves. The sun is silent but strong and seems almost to suspend all sound with its glare. It's noon, then it's 3pm, and then the sun starts to move downward, easing out. You relax. Say 'restart' to begin again or 'menu' to hear your options."
			response.append({
				'file': "05",
				'response': rep    
			})
		elif intent_type == 'BirchwoodShadeIntent':
			self.ContextManager.remove_context("BirchwoodFirstContext")
			self.ContextManager.handle_add_context("BirchwoodShadeContext")
			rep = "You are laying still in the grass. Sunlight dapples your torso. Your bare feet are in full sun, your eyes are fully shaded by a fabric canopy. You lie listening to the leaves. Shhhhhh. Shhhhh. Shhhh. Shhhh. Wiggle your toes. Does it begin to rain?"
			response.append({
				'file': "06",
				'response': rep    
			})

		elif intent_type == 'BirchwoodRainIntent':
			self.ContextManager.remove_context("BirchwoodShadeContext")
			rep = "A slow rain begins. It's the first time it's rained in months and the smell of the dry grass and leaves changes, shifts, mixes with the weight of the water. You feel the rain falling steadily on your body while your head, under the tent remains dry. The water drips onto the fabric above your head. Listen. Relax. Say 'restart' to begin again. Or say 'menu' to hear your options."
			response.append({
				'file': "07",
				'response': rep    
			})

		elif intent_type == 'BirchwoodNoRainIntent':
			self.ContextManager.remove_context("BirchwoodShadeContext")
			rep = "The sun goes entirely behind a cloud before emerging again in full brilliance, and then another cloud. You notice this only through the feeling of the light, as your eyes are closed. Time slows, time becomes the clouds. You relax. Say 'restart' to begin again. Or say 'menu' to hear your options."
			response.append({
				'file': "08",
				'response': rep    
			})
		elif intent_type == 'BirchwoodSmellIntent':
			self.ContextManager.remove_context("BirchwoodSunContext")
			rep = "It hasn't rained for months and the dry grass and leaves combined to form a smell that reminds you of childhood summers. The height of August when the air is full of water that hasn't fallen. The breeze sometimes brings you the gathered scent of the flowers in the field. It comes, and it goes, and sometimes the breeze brings also the smell of dust. You relax. Say 'restart' to begin again. Or say 'menu' to hear your options."
			response.append({
				'file': "09",
				'response': rep    
			})
		elif intent_type == 'HomePlanetIntent':
			self.ContextManager.remove_context("Question1Context")
			self.ContextManager.handle_add_context("HomePlanetContext")
			rep = "My planet is a place of tentacles. When we Ohaiglo return, our tentacles connect to the many-armed being and we at first adjoin the tentacles before we are pulled into them and absorbed. My planet would understand your limbs as tentacles and absorb you similarly. Do you want to focus on the senstation or the sound of the aborption?"
			response.append({
				'file': "10",
				'response': rep    
			})
		elif intent_type == 'HomePlanetSoundIntent':
			self.ContextManager.remove_context("HomePlanetContext")
			rep = "At first it is as though your hands and legs are handled gently by a skin that feels both like yours but also unfamiliar. They are stroked, and you hear at first the light scratch of skin on skin. As you are absorbed, the sound becomes more refined, like sugar falling into water in a steady stream. Right before you fall into a deep slumber, the sound of sugar becomes deeper and slower, as though your entire body were resonated by an enormous beating heart. You relax completely. Say 'restart' to begin again or 'menu' to hear your options."
			response.append({
				'file': "12",
				'response': rep    
			})
		elif intent_type == 'HomePlanetSensationIntent':
			self.ContextManager.remove_context("HomePlanetContext")
			rep = "Absorption is not scary. At first, for humans, it is like you are held with a steady grip on your heads and legs, by many people who come to you with good intentions. The grip turns into a reassuring weight. Feel it moving from your feet, to your shins to your thighs. Likewise, from your hands, to arms, to shoulders until your body is completely relaxed under a reassuring heaviness. The light disappears. You fall into a deep slumber, in a state of deep ease. Say 'restart' to begin again or 'menu' to hear your options."
			response.append({
				'file': "13",
				'response': rep    
			})
		elif intent_type == 'QuitIntent':
			self.ContextManager.clear_context()
			cherrypy.lib.sessions.expire()
			rep = f"Goodbye!"
			response.append({
				'file': "11",
				'response': rep    
			})
		elif intent_type == 'MenuIntent':
			self.ContextManager.clear_context()
			cherrypy.session["activeSkill"] = ""
			cherrypy.session["LastUtteranceCount"] = 0
			rep = "Let me query my tentacles. I'm told these are the options: I can guide you through a meditation. Or I can tell you more about ASMR, tell you about SOOTHER, or recommend ASMR content."
			response.append({
				'file': "14",
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

