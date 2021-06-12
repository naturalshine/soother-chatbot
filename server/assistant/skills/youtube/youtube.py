#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import requests

from .api.search import search_youtube
from Skill import Skill
from padatious import IntentContainer


class youtube_skill(Skill):

    def __init__(self, root_dir, name, nlp, active, hasContext):
        hasContext = True
        super(youtube_skill, self).__init__(root_dir, name, nlp, active, hasContext)


    def handle(self, intent_parser_result, text, latitude, longitude):

        skill_response = []
        context = intent_parser_result.matches
        for key, value in context.items():
            context[key] = context[key].replace("?","")

        data=search_youtube(context["keyword"])
        items=data['items']
        if len(items) > 0:
            for b in items:
                skill_response.append({
                    'title': b["snippet"]["title"],
                    'description': b["snippet"]["description"],
                    'url': "https://youtube.com/watch?v=" + b["id"]["videoId"]})
        else:
            skill_response.append({
                'title':'',
                'description':'Sorry we couldn\'t find %s on Youtube!' % context["keyword"],
                'url':''})

        return skill_response

