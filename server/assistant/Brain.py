#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import jsonpickle

import importlib
import cherrypy 

from nlp.cy.nlp import NaturalLanguageProcessing

class Brain(object):


    def __init__(self, online=True):
        self.skills = dict()
        self.nlp = NaturalLanguageProcessing()

        skills_root_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'skills')

        self.load_skill(skills_root_dir, 'spotify')
        self.load_skill(skills_root_dir, 'youtube')
        self.load_skill(skills_root_dir, 'tea')
        self.load_skill(skills_root_dir, 'Menu')
        self.load_skill(skills_root_dir, 'Personality')
        self.load_skill(skills_root_dir, 'asmr')
        self.load_skill(skills_root_dir, 'soother')

        if online:
            from RecordingsDatabase import RecordingsDatabase
            from skills_assistant_tasks import initialize_recordings_database_task, initialize_skills_database_task
            
            self.mysql_db = RecordingsDatabase()
            self.mysql_db.initialize()

            initialize_recordings_database_task.delay(self.expand_skills())
            initialize_skills_database_task.delay(self.list_skills())
           
 
    def get_skill_instance(self, skill_name):
        instance = self.skills[skillName]
        return instance

    def load_skill(self, skills_root_dir, skillname, active=True):
        skill_python_module = importlib.import_module('skills.%s.%s' % (skillname, skillname))
        class_ = getattr(skill_python_module, skillname + '_skill')
        hasContext = False
        instance = class_(skills_root_dir, skillname, self.nlp, active, hasContext)
        instance.hasContext = instance.get_context()
        self.skills[skillname] = instance


    def list_skills(self):
        skills = [] 
        for key in self.skills.keys():
            skills.append((key, self.skills[key].is_active()))
        return skills


    def get_unrecorded_sentence(self, uid):
        return self.mysql_db.select_random_unrecorded_sentence(uid)


    def handle_from_skill(self, text):
        best_key, best_intent = self.determine_intent(text)
        if best_key is not "" or best_key is not None: 
            cherrypy.log("BEST KEY")
            cherrypy.log(best_key)
            if len(best_key) > 0:
                cherrypy.session["activeSkill"] = best_key


        latitude=53.2303869
        longitude=-4.1299242
        if best_intent is not "" or best_intent is not None: 
            return self.handle_intent(best_key, best_intent, text, latitude, longitude)
            

    def handle(self, text, latitude=0.0, longitude=0.0):
        # Bangor, Gwynedd 
        cherrypy.log('alpha')
        if latitude==0.0 and longitude==0.0:
            latitude=53.2303869
            longitude=-4.1299242


        if 'activeSkill' not in cherrypy.session or cherrypy.session['activeSkill'] == "":
            best_key, best_intent = self.determine_intent(text)
            if best_key is not "" or best_key is not None: 
                cherrypy.log(best_key)

                if len(best_key) > 0:
                    cherrypy.session["activeSkill"] = best_key

        else: 
            currentSkill = cherrypy.session["activeSkill"]
            cherrypy.log(currentSkill)
            best_key, best_intent = self.determine_contextual_intent(text, currentSkill)

        if best_intent is not "" or best_intent is not None: 
            skill_result=self.handle_intent(best_key, best_intent, text, latitude, longitude)
            return best_key, skill_result
        else:
            return 'Sorry we could not find a match!', None


    def handle_intent(self, handler_key, intent, text, latitude, longitude):
        if(self.skills[handler_key].hasContext):
            if handler_key == "Menu_skill":
                ContextManager = self.skills["Personality_skill"].ContextManager
                return self.skills[handler_key].handle(text, cManager=ContextManager)
            else:
                return self.skills[handler_key].handle(text)
        else: 
            return self.skills[handler_key].handle_no_context(intent, text, latitude, longitude)
    
    def determine_contextual_intent(self, text, skillName):

        skillInstance = self.skills[skillName]

        adapt_confidence, intent = skillInstance.calculate_intent(text)

        return skillName, intent

    def determine_intent(self, text):
        best_intent = None
        best_handler = ''
        best_score = 0.0

        for key in self.skills.keys():
            adapt_confidence, intent = self.skills[key].calculate_intent(text)
            score=adapt_confidence*intent.conf
            if score > best_score:
                best_intent = intent
                best_handler = key
                best_score=score


        return best_handler, best_intent


    def expand_skills(self, include_additional_entities=False):
        result = {}
        for name in self.skills.keys():
            skill = self.skills.get(name)
            result[name] = skill.expand_intents(include_additional_entities)
        return result


if __name__ == "__main__":

    brain = Brain(online=False)

    if len(sys.argv) > 1:
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--text")
        parser.add_argument("-s", "--sentences", action='store_true')
        args = parser.parse_args()

        if args.text is not None:
            response = brain.handle(args.text)
            print (jsonpickle.encode(response))
        elif args.sentences is not None:
            response = brain.expand_skills(include_additional_entities=False)
            for skill in response:
                for intent in response[skill]:
                    for sentence in response[skill][intent]: 
                        if len(sentence)==0:
                            continue
                        if '{' in sentence and '}' in sentence:
                            continue
                        print (sentence)
        else:
            print ("Unknown")


