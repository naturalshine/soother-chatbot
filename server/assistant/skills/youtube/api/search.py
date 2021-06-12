#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
#from .apikey import CLIENT_ID, CLIENT_SECRET

# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
from .apikey import API_KEY
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def search_youtube(keyword):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = API_KEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        type="video",
        maxResults=3,
        q=keyword
    )

    response = request.execute()
    '''
    {
	  "kind": "youtube#searchListResponse",
	  "etag": etag,
	  "nextPageToken": string,
	  "prevPageToken": string,
	  "regionCode": string,
	  "pageInfo": {
	    "totalResults": integer,
	    "resultsPerPage": integer
	  },
	  "items": [
	    search Resource
	  ]
	}
	'''
    print(response)

    return response

if __name__ == "__main__":
    print (search_youtube(sys.argv[1]))
