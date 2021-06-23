#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import requests

from .api.search import search_youtube
from .intents import (entities, single_regex_entities, skill_intents)
from Skill import Skill
import cherrypy
from Brain import Brain
from padatious import IntentContainer


class youtube_skill(Skill):

    def __init__(self, root_dir, name, nlp, active, hasContext):
        hasContext = False
        Context = []
        favoriteGenre = ""
        rolePlayGenre = ""
        super(youtube_skill, self).__init__(root_dir, name, nlp, active, hasContext)

    def act_on_intent(self, intent, text):
        response = ""
       
        """
        Chooses proper action to take based on intent.

        :param dict intent: 

        """


        intent_type = intent['intent_type']
        cherrypy.log(intent_type)
        if intent_type == 'SearchIntent':
            self.ContextManager.handle_add_context("FavoriteVideoContext")
            response = "Do you have a favorite kind of ASMR video?"
        
        elif intent_type == "AboutAsmrIntent":
            response = "ASMR is Autonomous Sensory Meridian Response. It describes a tingling in the scalp and spine in response to soft sounds like whispering, nail-tapping, or hair-brushing."    

        elif intent_type == 'FavoriteVideoIntent':
            self.ContextManager.handle_add_context("WatchFavoriteVideoContext")            
            response = "What is it?"

        elif intent_type == 'YesFavoriteVideoIntent':
            self.ContextManager.remove_context("FavoriteVideoContext")
            self.ContextManager.handle_add_context("WatchFavoriteVideoContext")
            if "GenreKeyword" in intent:
                self.favoriteGenre = intent["GenreKeyword"]
            elif "RolePlayKeyword" in intent:
                self.favoriteGenre = intent["RolePlayKeyword"]
            elif "keyword" in self.Context:
                self.favoriteGenre = self.Context['keyword']

            if self.favoriteGenre is not '':
                response = f"I also love {self.favoriteGenre}. Would you like to watch that?"
            else: 
                self.favoriteGenre = text
                response = "I love that too! Would you like to watch one of those?"

        elif intent_type == 'NoFavoriteVideoIntent':
            self.ContextManager.remove_context("FavoriteVideoContext")
            self.ContextManager.handle_add_context("TriggerSampleContext")
            response = "No problem. Sometimes it's good to start with a medeley of ASMR triggers. Would you like to watch one of those?"
        
        elif intent_type == "WatchFavoriteVideoIntent":
            self.ContextManager.remove_context("WatchFavoriteVideoContext")
            self.ContextManager.handle_add_context("ProvideVideoContext")
            cherrypy.session["activeSkill"] = None
            cherrypy.session["LastUtteranceCount"] = 0
            if self.favoriteGenre is not '':
                self.favoriteGenre = self.favoriteGenre + " asmr"
                response = []
                data=search_youtube(self.favoriteGenre)
                items=data['items']
                if len(items) > 0:
                    response.append({
                        'response': f'Here\'s a {self.favoriteGenre} video for you!',
                        'title': items[0]["snippet"]["title"],
                        'description': items[0]["snippet"]["description"],
                        'url': "https://youtube.com/watch?v=" + items[0]["id"]["videoId"]})
                else:
                    response.append({
                        'response': f'Sorry we couldn\'t find {self.favoriteGenre} on Youtube!',
                        'title':'',
                        'description':'',
                        'url':''})
        
        elif intent_type == "NoWatchFavoriteVideoIntent":
            self.ContextManager.remove_context("WatchFavoriteVideoContext")
            self.ContextManager.handle_add_context("RolePlayContext")
            response = "No problem. I love role-play videos. Would you like to watch one of those?"

        elif intent_type == "YesRolePlayVideoIntent":
            self.ContextManager.remove_context("RolePlayContext")
            self.ContextManager.handle_add_context("RolePlayGenreContext")
            response = "What's your favorite role play type?"

        elif intent_type == "NoRolePlayVideoIntent":
            self.ContextManager.remove_context("RolePlayContext")
            self.ContextManager.handle_add_context("NailTappingVideo")
            response = "I get it, role plays can be annoying. How an hour of nails tapping?"


        elif intent_type == "RolePlayGenreIntent":
            self.ContextManager.remove_context("RolePlayGenreContext")
            self.ContextManager.handle_add_context("ProvideVideoContext")
            cherrypy.session["activeSkill"] = None
            cherrypy.session["LastUtteranceCount"] = 0

            if "RolePlayKeyword" in intent:
                self.rolePlayGenre = intent["RolePlayKeyword"]
                reply = f"Here's a {self.rolePlayGenre} ASMR role play!"
            elif "keyword" in self.Context:
                self.rolePlayGenre = self.Context['keyword']
                reply = f"Here's a {self.rolePlayGenre} ASMR role play!"
            else: 
                self.rolePlayGenre = "egyptian tomb imp"
                reply = f"I'm sorry I couldn't understand you! Here's an {self.rolePlayGenre} ASMR role play!"

            response = []
            data=search_youtube(self.rolePlayGenre + " asmr")
            items=data['items']
            if len(items) > 0:
                response.append({
                    'response': reply,
                    'title': items[0]["snippet"]["title"],
                    'description': items[0]["snippet"]["description"],
                    'url': "https://youtube.com/watch?v=" + items[0]["id"]["videoId"]})
            else:
                response.append({
                    'response': f'Sorry we couldn\'t find {self.rolePlayGenre} on Youtube!',
                    'title':'',
                    'description':'',
                    'url':''})
            

        elif intent_type == "NoRolePlayGenreIntent":
            self.ContextManager.remove_context("RolePlayGenreContext")
            self.ContextManager.handle_add_context("ProvideVideoContext")
            cherrypy.session["activeSkill"] = None
            cherrypy.session["LastUtteranceCount"] = 0

            response = []
            data=search_youtube("lost in forest ASMR")
            items=data['items']
            if len(items) > 0:
                response.append({
                    'response': "I love lost in forest ASMR videos. Here you go!",
                    'title': items[0]["snippet"]["title"],
                    'description': items[0]["snippet"]["description"],
                    'url': "https://youtube.com/watch?v=" + items[0]["id"]["videoId"]})
            else:
                response.append({
                    'response': f'Sorry I couldn\'t find what I was looking for on Youtube!',
                    'title':'',
                    'description':'',
                    'url':''})
            
        elif intent_type == "YesTriggerVideoIntent":
            self.ContextManager.remove_context("TriggerSampleContext")
            self.ContextManager.handle_add_context("ProvideVideoContext")
            cherrypy.session["activeSkill"] = None
            cherrypy.session["LastUtteranceCount"] = 0

            response = []
            data=search_youtube("ASMR triggers")
            items=data['items']
            if len(items) > 0:
                response.append({
                    'response': "Here's a great ASMR trigger video for you!",
                    'title': items[0]["snippet"]["title"],
                    'description': items[0]["snippet"]["description"],
                    'url': "https://youtube.com/watch?v=" + items[0]["id"]["videoId"]})
            else:
                response.append({
                    'response': f'Sorry I couldn\'t find what I was looking for on Youtube!',
                    'title':'',
                    'description':'',
                    'url':''})

        elif intent_type == "NoTriggerVideoIntent":
            self.ContextManager.remove_context("TriggerSampleContext")
            self.ContextManager.handle_add_context("NailTappingVideo")
            response = "How about an hour of nail-tapping?"

        elif intent_type == "YesNailsVideoIntent":
            self.ContextManager.remove_context("NailTappingVideo")
            self.ContextManager.handle_add_context("ProvideVideoContext")
            cherrypy.session["activeSkill"] = None
            cherrypy.session["LastUtteranceCount"] = 0

            response = []
            data=search_youtube("ASMR nails hour")
            items=data['items']
            if len(items) > 0:
                response.append({
                    'response': "Here's an hour of nail-tapping for you!",
                    'title': items[0]["snippet"]["title"],
                    'description': items[0]["snippet"]["description"],
                    'url': "https://youtube.com/watch?v=" + items[0]["id"]["videoId"]})
            else:
                response.append({
                    'response': f'Sorry I couldn\'t find what I was looking for on Youtube!',
                    'title':'',
                    'description':'',
                    'url':''})

        elif intent_type == "NoNailsVideoIntent":
            self.ContextManager.remove_context("NailTappingVideo")
            self.ContextManager.handle_add_context("ProvideVideoContext")
            cherrypy.session["activeSkill"] = None
            cherrypy.session["LastUtteranceCount"] = 0

            response = []
            data=search_youtube("ASMR ephemeral rift")
            items=data['items']
            if len(items) > 0:
                response.append({
                    'response': "OK, here's a great ASMRtist instead",
                    'title': items[0]["snippet"]["title"],
                    'description': items[0]["snippet"]["description"],
                    'url': "https://youtube.com/watch?v=" + items[0]["id"]["videoId"]})
            else:
                response.append({
                    'response': f'Sorry I couldn\'t find what I was looking for on Youtube!',
                    'title':'',
                    'description':'',
                    'url':''})


 
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

    def handle_no_context(self, intent_parser_result, text, latitude, longitude):

        skill_response = []

        context = intent_parser_result.matches
        for key, value in context.items():
            context[key] = context[key].replace("?","")
    
        self.Context = context

        engineEntities = {"entities" : entities, "single_regex_entities" : single_regex_entities, "skill_intents": skill_intents}

        skill_response = self.run_intent(text, engineEntities)

        return skill_response

